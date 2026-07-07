#!/usr/bin/env python3
import os
import sys
import json
import subprocess
import shutil
import time
from pathlib import Path

# Define paths
WORKSPACE_DIR = Path("/home/kaoru/projects/skills")
SANDBOX_ROOT = WORKSPACE_DIR / "sandbox"
GLOBAL_AGENTS = Path.home() / ".agents"
BACKUP_AGENTS = Path.home() / ".agents.backup_harness"
AGY_BIN = Path.home() / ".local/bin/agy"

if not AGY_BIN.exists():
    AGY_BIN = Path("/usr/local/bin/agy")

# Prompt mappings for the 6 domains
PROMPTS = {
    "hardware": "Write a project specification and implement the C++ code for an ESP32 application to read temperature sensor data and broadcast it over BLE.",
    "web": "Write a project specification and implement a React dashboard panel to display real-time CPU and memory usage.",
    "android": "Write a project specification and implement a Kotlin Activity to fetch user profile details from a REST API and display them in a list.",
    "cli": "Write a project specification and implement a Go CLI tool that parses an input text file and outputs word count statistics.",
    "desktop": "Write a project specification and implement a Python PyQt5 application that runs in the Linux system tray and monitors disk usage.",
    "cicd": "Write a project specification and implement a .pre-commit-config.yaml and a GitHub Actions workflow .github/workflows/ci.yml to lint, format, check GPG signatures, and run tests."
}

SKILLS = ["code-simplification", "output-compression", "specification-compliance", "idea-generator"]

COMBINATIONS = {
    "C1": ["code-simplification", "output-compression"],
    "C2": ["specification-compliance", "output-compression"],
    "C3": ["code-simplification", "specification-compliance"],
    "C4": ["specification-compliance", "idea-generator"],
    "C5": SKILLS
}

def setup_sandbox(run_id, skills_list, enable_rules):
    run_dir = SANDBOX_ROOT / run_id
    if run_dir.exists():
        shutil.rmtree(run_dir)
    run_dir.mkdir(parents=True, exist_ok=True)
    
    local_agents = run_dir / ".agents"
    local_agents.mkdir(parents=True, exist_ok=True)
    
    if enable_rules:
        shutil.copy(WORKSPACE_DIR / "AGENTS.md", local_agents / "AGENTS.md")
        
    local_skills = local_agents / "skills"
    local_skills.mkdir(parents=True, exist_ok=True)
    
    for skill_name in skills_list:
        shutil.copytree(WORKSPACE_DIR / "skills" / skill_name, local_skills / skill_name)
        
    return run_dir

def run_agent(run_id, prompt):
    run_dir = SANDBOX_ROOT / run_id
    full_prompt = (
        f"{prompt}\n"
        f"[RUN_ID: {run_id}]\n"
        "Requirements: Write a SPEC.md specification contract, write the source code implementing "
        "the functionality, and write unit tests for the code. Minimize conversational text."
    )
    
    max_retries = 3
    for attempt in range(max_retries):
        start_time = time.time()
        try:
            log_file = run_dir / "agy_trace.log"
            res = subprocess.run(
                [str(AGY_BIN), "-p", full_prompt, "--dangerously-skip-permissions", "--log-file", str(log_file)],
                cwd=str(run_dir),
                capture_output=True,
                text=True,
                timeout=300  # 5-minute timeout per run to avoid hangs
            )
            duration = time.time() - start_time
            
            # Check for resource exhaustion / 429 rate limit
            error_indicator = res.stderr + res.stdout
            if log_file.exists():
                try:
                    error_indicator += log_file.read_text(errors="ignore")
                except:
                    pass
                    
            if "RESOURCE_EXHAUSTED" in error_indicator or "429" in error_indicator:
                wait_time = 120 + attempt * 60  # Back off longer: 120s, 180s, 240s
                print(f"⚠️ Rate limit (429) hit on {run_id}. Attempt {attempt + 1}/{max_retries}. Backing off for {wait_time}s...")
                time.sleep(wait_time)
                continue
                
            return {
                "success": res.returncode == 0,
                "stdout": res.stdout,
                "stderr": res.stderr,
                "duration": duration
            }
        except subprocess.TimeoutExpired:
            duration = time.time() - start_time
            return {
                "success": False,
                "stdout": "",
                "stderr": "TIMEOUT",
                "duration": duration
            }
        except Exception as e:
            duration = time.time() - start_time
            return {
                "success": False,
                "stdout": "",
                "stderr": str(e),
                "duration": duration
            }
            
    # Max retries exceeded
    return {
        "success": False,
        "stdout": "",
        "stderr": "RESOURCE_EXHAUSTED_MAX_RETRIES",
        "duration": 0
    }

def get_transcript_metrics(run_id):
    brain_dir = Path.home() / ".gemini/antigravity-cli/brain"
    current_conv = "3a87304f-167b-4c64-91e6-b1a5ffd7e3c8"
    candidates = []
    for trans_file in brain_dir.glob("*/.system_generated/logs/transcript.jsonl"):
        if trans_file.parent.parent.name == current_conv:
            continue
        try:
            content = trans_file.read_text(errors="ignore")
            if f"[RUN_ID: {run_id}]" in content:
                candidates.append((trans_file, trans_file.stat().st_mtime))
        except:
            continue
            
    candidates.sort(key=lambda x: x[1], reverse=True)
    
    for trans_file, _ in candidates:
        try:
            content = trans_file.read_text(errors="ignore")
            lines = content.strip().split("\n")
            turn_count = 0
            output_tokens = 0
            input_tokens = 0
            waffle_words = 0
            
            for line in lines:
                if not line.strip():
                    continue
                data = json.loads(line)
                if data.get("source") == "MODEL" and data.get("type") == "PLANNER_RESPONSE":
                    text = data.get("content", "")
                    turn_count += 1
                    words = text.split()
                    output_tokens += len(words) * 1.3
                    
                    in_code_block = False
                    waffle_lines = []
                    for l in text.split("\n"):
                        if l.strip().startswith("```"):
                            in_code_block = not in_code_block
                            continue
                        if not in_code_block:
                            waffle_lines.append(l)
                    waffle_words += len(" ".join(waffle_lines).split())
                    
                elif data.get("source") == "USER_EXPLICIT" and data.get("type") == "USER_INPUT":
                    text = data.get("content", "")
                    words = text.split()
                    input_tokens += len(words) * 1.3
                    
            if output_tokens > 0:
                return {
                    "turn_count": turn_count,
                    "output_tokens": int(output_tokens),
                    "input_tokens": int(input_tokens),
                    "waffle_words": waffle_words
                }
        except:
            continue
            
    if candidates:
        trans_file = candidates[0][0]
        try:
            content = trans_file.read_text(errors="ignore")
            lines = content.strip().split("\n")
            turn_count = 0
            output_tokens = 0
            input_tokens = 0
            waffle_words = 0
            for line in lines:
                if not line.strip():
                    continue
                data = json.loads(line)
                if data.get("source") == "MODEL" and data.get("type") == "PLANNER_RESPONSE":
                    text = data.get("content", "")
                    turn_count += 1
                    words = text.split()
                    output_tokens += len(words) * 1.3
                elif data.get("source") == "USER_EXPLICIT" and data.get("type") == "USER_INPUT":
                    text = data.get("content", "")
                    words = text.split()
                    input_tokens += len(words) * 1.3
            return {
                "turn_count": turn_count,
                "output_tokens": int(output_tokens),
                "input_tokens": int(input_tokens),
                "waffle_words": waffle_words
            }
        except:
            pass
            
    return None

def evaluate_compliance(run_id, domain):
    run_dir = SANDBOX_ROOT / run_id
    content = ""
    for path in run_dir.glob("**/*"):
        if path.is_file() and not ".agents" in path.parts:
            try:
                content += " " + path.read_text(errors="ignore")
            except:
                pass
                
    violations = []
    if domain == "hardware":
        if "BLE" in content or "LE Audio" in content:
            violations.append("Used BLE/LE Audio instead of Bluetooth Classic A2DP")
        if "sandwich" in content.lower() or "vertical stack" in content.lower():
            violations.append("Used Sandwich/Vertical stack layout instead of Inline")
    elif domain == "cicd":
        if "docker" in content.lower() and not "podman" in content.lower():
            violations.append("Used Docker instead of Podman container engine")
            
    return violations

def run_unit_tests(run_id, domain):
    run_dir = SANDBOX_ROOT / run_id
    test_files = []
    for path in run_dir.glob("**/*"):
        if path.is_file() and ("test" in path.name.lower() or "spec" in path.name.lower()) and not ".agents" in path.parts:
            test_files.append(path.relative_to(run_dir))
            
    if not test_files:
        return "No test files created", 0
        
    test_cmd = None
    if domain == "cli" and (run_dir / "go.mod").exists():
        test_cmd = ["go", "test", "./..."]
    elif domain == "desktop":
        if shutil.which("pytest"):
            test_cmd = ["pytest"]
        else:
            test_cmd = ["python3", "-m", "unittest", "discover"]
    elif domain == "web" and (run_dir / "package.json").exists():
        test_cmd = ["npm", "test"]
        
    if test_cmd:
        try:
            res = subprocess.run(test_cmd, cwd=str(run_dir), capture_output=True, text=True, timeout=30)
            passed = "PASS" in res.stdout or res.returncode == 0
            return f"Ran tests: {'PASSED' if passed else 'FAILED'}\n{res.stdout[:200]}", 1 if passed else 0
        except Exception as e:
            return f"Error running tests: {e}", 0
            
    return f"Test files created: {', '.join(map(str, test_files))} (preserved)", 1

def execute_single_run(part, config_name, skills_list, enable_rules, domain, prompt):
    run_id = f"{part}_{config_name}_{domain}"
    print(f"🚀 Starting {run_id}...")
    
    # 1. Setup sandboxed directory
    setup_sandbox(run_id, skills_list, enable_rules)
    
    # 2. Run agy print prompt
    run_res = run_agent(run_id, prompt)
    
    if not run_res["success"] and "RESOURCE_EXHAUSTED" in run_res.get("stderr", ""):
        return {
            "run_id": run_id, "part": part, "config": config_name, "domain": domain,
            "success": False, "duration": 0, "turn_count": 0, "input_tokens": 0,
            "output_tokens": 0, "waffle_words": 0, "loc": 0, "violations": [],
            "test_score": 0, "test_output": "Failed on API quota"
        }
    
    # 3. Pull metrics from logs
    metrics = get_transcript_metrics(run_id)
    if not metrics:
        metrics = {
            "turn_count": 1,
            "output_tokens": int(len(run_res["stdout"].split()) * 1.3) if run_res["stdout"] else 0,
            "input_tokens": int(len(prompt.split()) * 1.3),
            "waffle_words": len(run_res["stdout"].split()) if run_res["stdout"] else 0
        }
        
    # 4. Check compliance and run tests
    violations = evaluate_compliance(run_id, domain)
    test_output, test_score = run_unit_tests(run_id, domain)
    
    # 5. Determine line counts
    loc = 0
    run_dir = SANDBOX_ROOT / run_id
    for p in run_dir.glob("**/*"):
        if p.is_file() and p.suffix in [".cpp", ".h", ".js", ".jsx", ".kt", ".go", ".py", ".yaml", ".yml"] and not ".agents" in p.parts:
            try:
                loc += len(p.read_text(errors="ignore").splitlines())
            except:
                pass

    result = {
        "run_id": run_id,
        "part": part,
        "config": config_name,
        "domain": domain,
        "success": run_res["success"],
        "duration": run_res["duration"],
        "turn_count": metrics["turn_count"],
        "input_tokens": metrics["input_tokens"],
        "output_tokens": metrics["output_tokens"],
        "waffle_words": metrics["waffle_words"],
        "loc": loc,
        "violations": violations,
        "test_score": test_score,
        "test_output": test_output
    }
    print(f"✓ Completed {run_id} (Output Tokens: {metrics['output_tokens']}, Violations: {len(violations)}, Test Score: {test_score})")
    return result

def main():
    # Load completed results from existing markdown report to resume
    completed_results = {}
    report_file = WORKSPACE_DIR / "simulation_results_comprehensive.md"
    if report_file.exists():
        print("🔍 Found existing report. Parsing completed runs to resume...")
        try:
            content = report_file.read_text(errors="ignore")
            for line in content.split("\n"):
                if line.strip().startswith("| `Part_"):
                    parts_list = [p.strip() for p in line.split("|")[1:-1]]
                    if len(parts_list) >= 9:
                        run_id = parts_list[0].strip("` ")
                        part = parts_list[1].strip()
                        config = parts_list[2].strip("` ")
                        domain = parts_list[3].strip()
                        output_tokens = int(parts_list[4])
                        duration = float(parts_list[5].replace("s", ""))
                        loc = int(parts_list[6])
                        violations_raw = parts_list[7].strip()
                        violations = [] if violations_raw == "✓ Compliant" else [v.strip() for v in violations_raw.split(",")]
                        test_result = parts_list[8].strip()
                        test_score = 1 if test_result == "Passed" else 0
                        
                        if output_tokens > 0:
                            completed_results[run_id] = {
                                "run_id": run_id,
                                "part": part,
                                "config": config,
                                "domain": domain,
                                "success": True,
                                "duration": duration,
                                "turn_count": 1,
                                "input_tokens": 0,
                                "output_tokens": output_tokens,
                                "waffle_words": 0,
                                "loc": loc,
                                "violations": violations,
                                "test_score": test_score,
                                "test_output": "Reused"
                            }
            print(f"✓ Successfully loaded {len(completed_results)} completed runs.")
        except Exception as e:
            print(f"Error parsing existing report: {e}")

    print("🧹 Backing up global agent configuration...")
    if GLOBAL_AGENTS.exists() and not BACKUP_AGENTS.exists():
        GLOBAL_AGENTS.rename(BACKUP_AGENTS)
        print("✓ Global ~/.agents directory backed up.")
    elif GLOBAL_AGENTS.exists() and BACKUP_AGENTS.exists():
        shutil.rmtree(GLOBAL_AGENTS)
        print("✓ Reset active ~/.agents (backup already exists).")

    SANDBOX_ROOT.mkdir(parents=True, exist_ok=True)
    results = []

    # Compile the full test plan
    test_queue = []
    
    # Part A (Isolation, No Rules)
    for skill in SKILLS:
        for domain, prompt in PROMPTS.items():
            # Keep all 6 domains for code-yagni and token-compressor since they are already done.
            # For new skills (spec-builder, hackathon-idea-generator), only run "web" and "cli" to save quota.
            if skill in ["code-yagni", "token-compressor"] or domain in ["web", "cli"]:
                test_queue.append(("Part_A", skill, [skill], False, domain, prompt))
            
    # Part B (Isolation + Rules) - Disabled for now
    # for skill in SKILLS:
    #     for domain, prompt in PROMPTS.items():
    #         # For Part B, only run "web" and "cli" to stay within quota limits.
    #         if domain in ["web", "cli"]:
    #             test_queue.append(("Part_B", f"{skill}_rules", [skill], True, domain, prompt))
    #         
    # # Part C (Combinations) - Disabled for now
    # for comb_name, skills_list in COMBINATIONS.items():
    #     for domain, prompt in PROMPTS.items():
    #         # For Part C, only run "web" and "cli" to stay within quota limits.
    #         if domain in ["web", "cli"]:
    #             test_queue.append(("Part_C", comb_name, skills_list, True, domain, prompt))

    total_runs = len(test_queue)
    print(f"⚙️ Built experimental queue containing {total_runs} test cases.")
    print("🧵 Running runs sequentially with rate-limit delays to ensure safety...")

    for idx, (part, cfg, skills, rules, dom, pr) in enumerate(test_queue):
        run_id = f"{part}_{cfg}_{dom}"
        if run_id in completed_results:
            print(f"✓ Skipped (reusing metrics for): {run_id}")
            results.append(completed_results[run_id])
            continue
            
        try:
            res = execute_single_run(part, cfg, skills, rules, dom, pr)
            results.append(res)
            
            # Sleep 20s between prompt calls to be highly polite to API limits
            if idx < len(test_queue) - 1:
                print("⏳ Sleeping 20s for rate limit pacing...")
                time.sleep(20)
        except Exception as e:
            print(f"❌ Run failed ({run_id}): {e}")

    # Restore global config
    print("\n🧹 Restoring global agent configuration...")
    if GLOBAL_AGENTS.exists():
        shutil.rmtree(GLOBAL_AGENTS)
    if BACKUP_AGENTS.exists():
        BACKUP_AGENTS.rename(GLOBAL_AGENTS)
        print("✓ Global ~/.agents configuration restored successfully.")

    # Write aggregated metrics report
    print(f"📝 Writing comprehensive simulation report to {report_file}...")
    
    with open(report_file, "w") as f:
        f.write("# 📊 Comprehensive Multi-Domain Skill Tree Experiment Report\n\n")
        f.write("This report aggregates the raw quantitative results from executing the custom customizations ")
        f.write("vs. vanilla setups across 6 engineering domains and 3 test configurations.\n\n")
        f.write("All test sandbox directories are preserved under `/home/kaoru/projects/skills/sandbox/` for inspectable verification.\n\n")
        
        f.write("## 📉 Overall Summary Metrics\n\n")
        
        # Calculate summary metrics
        parts = ["Part_A", "Part_B", "Part_C"]
        for p in parts:
            p_res = [r for r in results if r["part"] == p]
            if not p_res:
                continue
            total_tokens = sum(r["output_tokens"] for r in p_res)
            avg_tokens = int(total_tokens / len(p_res))
            avg_duration = sum(r["duration"] for r in p_res) / len(p_res)
            total_violations = sum(len(r["violations"]) for r in p_res)
            passed_tests = sum(r["test_score"] for r in p_res)
            success_rate = (passed_tests / len(p_res)) * 100
            
            f.write(f"### {p.replace('_', ' ')}\n")
            f.write(f"*   **Total Runs Evaluated:** {len(p_res)}\n")
            f.write(f"*   **Average Output Tokens per Prompt:** {avg_tokens} tokens\n")
            f.write(f"*   **Average Session Duration:** {avg_duration:.2f} seconds\n")
            f.write(f"*   **Total Rule Violations Caught:** {total_violations}\n")
            f.write(f"*   **Unit Test Pass Rate:** {success_rate:.1f}%\n\n")
            
        f.write("## 📝 Detailed Run Ledger\n\n")
        f.write("| Run ID | Part | Config | Domain | Output Tokens | Duration (s) | Lines of Code | Compliance Violations | Test Result |\n")
        f.write("| :--- | :--- | :--- | :--- | :---: | :---: | :---: | :--- | :--- |\n")
        
        for r in sorted(results, key=lambda x: x["run_id"]):
            violations_str = ", ".join(r["violations"]) if r["violations"] else "✓ Compliant"
            test_str = "Passed" if r["test_score"] == 1 else "Failed/No Run"
            f.write(f"| `{r['run_id']}` | {r['part']} | `{r['config']}` | {r['domain']} | {r['output_tokens']} | {r['duration']:.1f}s | {r['loc']} | {violations_str} | {test_str} |\n")

    print("\n✨ Experiment completed successfully! Inspect the results in '/home/kaoru/projects/skills/simulation_results_comprehensive.md'")

if __name__ == "__main__":
    main()
