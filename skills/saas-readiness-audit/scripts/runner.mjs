#!/usr/bin/env node
// Deterministic audit loop for saas-readiness-audit.
// Usage: READINESS_PHASE=audit node runner.mjs <repo-dir> [--only ID1,ID2]
// Probe exit contract: 0 PASS, 1 FAIL, 3 PARTIAL (partial_ok only), 2 ERROR.
// The agent does not choose what to run: this runner executes checks.yaml verbatim.
import fs from 'node:fs';
import path from 'node:path';
import { spawnSync } from 'node:child_process';
import { createRequire } from 'node:module';

const repo = path.resolve(process.argv[2] || '.');
const yaml = loadYaml(repo);
const onlyIdx = process.argv.indexOf('--only');
const only = onlyIdx > -1 ? new Set(process.argv[onlyIdx + 1].split(',')) : null;
const R = p => path.join(repo, '.readiness', p);
const phase = process.env.READINESS_PHASE || 'audit';
const ts = new Date();
const pad = n => String(n).padStart(2, '0');
const runId = `${ts.getUTCFullYear()}${pad(ts.getUTCMonth() + 1)}${pad(ts.getUTCDate())}-${pad(ts.getUTCHours())}${pad(ts.getUTCMinutes())}${pad(ts.getUTCSeconds())}-${phase}`;
const runDir = R(`runs/${runId}`);
fs.mkdirSync(path.join(runDir, 'probe-output'), { recursive: true });

let seq = 0;
const traceFd = fs.openSync(path.join(runDir, 'trace.jsonl'), 'a');
const trace = ev => { const e = { run_id: runId, ts: new Date().toISOString(), phase, seq: ++seq, ...ev }; fs.writeSync(traceFd, JSON.stringify(e) + '\n'); return e.seq; };

// --- context load (section 2 order) ---
const project = yaml.load(fs.readFileSync(R('project.yaml'), 'utf8'));
trace({ event: 'context_load', output_ref: '.readiness/project.yaml' });
const waivers = yaml.load(fs.readFileSync(R('waivers.yaml'), 'utf8')) || [];
trace({ event: 'context_load', output_ref: '.readiness/waivers.yaml', reason: `${waivers.length} waivers` });
if (fs.existsSync(R('LESSONS.md'))) trace({ event: 'context_load', output_ref: '.readiness/LESSONS.md', reason: 'informational only; cannot alter checks.yaml scope' });
const checks = yaml.load(fs.readFileSync(R('checks.yaml'), 'utf8')).filter(c => !only || only.has(c.id));
trace({ event: 'context_load', output_ref: '.readiness/checks.yaml', reason: `${checks.length} checks` });

const applies = expr => {
  const js = String(expr).replace(/'([^']+)'\s+in\s+(\w+)/g, (_, v, k) => `(${k}||[]).includes(${JSON.stringify(v)})`);
  return Boolean(Function(...Object.keys(project), `return (${js});`)(...Object.values(project)));
};
const today = ts.toISOString().slice(0, 10);
const STATUS = { 0: 'PASS', 1: 'FAIL', 3: 'PARTIAL' };
const findings = [];
let consecutiveEnvErrors = 0;

const runProbe = (cmd, partialOk) => {
  const r = spawnSync('bash', ['-c', cmd], { cwd: repo, encoding: 'utf8', timeout: 30000, env: { ...process.env, READINESS_PHASE: phase, PARTIAL_OK: partialOk ? '1' : '0' } });
  const env_error = r.error || r.signal || r.status === 2 || r.status == null || ![0, 1, 3].includes(r.status);
  return { exit: r.status, out: `$ ${cmd}\n--- stdout ---\n${r.stdout || ''}\n--- stderr ---\n${r.stderr || ''}${r.error ? '\n' + r.error.message : ''}`, env_error };
};

for (const c of checks.sort((a, b) => a.tier - b.tier)) {
  const base = { check_id: c.id, tier: c.tier, confidence: c.confidence, fix_policy: c.fix_policy, waiver: null };
  if (!applies(c.applies_if)) { const s = trace({ check_id: c.id, event: 'decision', status: 'N/A', reason: `applies_if false: ${c.applies_if}` }); findings.push({ ...base, status: 'N/A', evidence: `applies_if: ${c.applies_if}`, trace_seq: s }); continue; }
  const w = waivers.find(x => x.check_id === c.id);
  if (w && w.expires >= today) { const s = trace({ check_id: c.id, event: 'decision', status: 'WAIVED', reason: `waiver ${w.id} until ${w.expires}` }); findings.push({ ...base, status: 'WAIVED', waiver: w.id, evidence: w.reason, trace_seq: s }); continue; }
  if (w) trace({ check_id: c.id, event: 'decision', reason: `waiver ${w.id} EXPIRED ${w.expires}; running check` });

  if (c.probe.kind === 'manual') {
    const key = c.probe.run.replace('attestation:', '');
    const att = project.attestations?.[key];
    const status = att ? 'PASS' : 'UNRUN';
    const s = trace({ check_id: c.id, event: 'decision', status, reason: att ? `attested: ${att}` : `no human attestation for '${key}' in project.yaml` });
    findings.push({ ...base, status, evidence: att ? `attestation ${key}=${att}` : 'needs human attestation', trace_seq: s });
    continue;
  }

  trace({ check_id: c.id, event: 'probe_start', cmd: c.probe.run });
  let res = runProbe(c.probe.run, c.partial_ok);
  if (res.env_error) { trace({ check_id: c.id, event: 'tool_error', cmd: c.probe.run, exit: res.exit }); trace({ check_id: c.id, event: 'retry', cmd: c.probe.run }); res = runProbe(c.probe.run, c.partial_ok); }
  const ref = `probe-output/${c.id}.txt`;
  fs.writeFileSync(path.join(runDir, ref), res.out);
  const contractViolation = res.exit === 3 && !c.partial_ok;
  if (contractViolation) trace({ check_id: c.id, event: 'probe_suspect', exit: 3, reason: 'probe returned PARTIAL but check is not partial_ok' });
  const status = res.env_error || contractViolation ? 'ERROR' : STATUS[res.exit];
  const excerpt = res.out.split('\n').filter(l => /^(ok|FAIL|RESULT)|:\d+:/.test(l)).slice(0, 8).join(' | ');
  const s = trace({ check_id: c.id, event: 'probe_end', cmd: c.probe.run, exit: res.exit, status, output_ref: ref });
  findings.push({ ...base, status, evidence: `${ref} :: ${excerpt}`.slice(0, 400), trace_seq: s });

  consecutiveEnvErrors = res.env_error ? consecutiveEnvErrors + 1 : 0;
  if (consecutiveEnvErrors >= 3) { trace({ event: 'stop', reason: 'environment broken: 3 consecutive ERRORs' }); trace({ event: 'escalation', reason: 'fix environment before re-running' }); break; }
}
for (const c of checks) if (!findings.some(f => f.check_id === c.id)) { const s = trace({ check_id: c.id, event: 'decision', status: 'UNRUN', reason: 'run stopped early' }); findings.push({ check_id: c.id, tier: c.tier, status: 'UNRUN', confidence: c.confidence, fix_policy: c.fix_policy, evidence: 'not run', trace_seq: s, waiver: null }); }

fs.writeFileSync(path.join(runDir, 'findings.jsonl'), findings.map(f => JSON.stringify(f)).join('\n') + '\n');

// --- verdict (computed, section 10) ---
const t0 = findings.filter(f => f.tier === 0);
const blocking = t0.filter(f => ['FAIL', 'ERROR', 'UNRUN', 'DISPUTED', 'PARTIAL'].includes(f.status));
const judgementOnly = t0.filter(f => f.status === 'PASS' && f.confidence === 'judgement');
const t1gaps = findings.filter(f => f.tier === 1 && !['PASS', 'N/A', 'WAIVED'].includes(f.status));
const verdict = blocking.length ? 'Not ready' : judgementOnly.length ? 'Not ready: needs human attestation' : t1gaps.length ? 'Ship with known gaps' : 'Ship';
trace({ event: 'stop', reason: `complete; verdict=${verdict}` });

// diff vs previous run
const prev = fs.readdirSync(R('runs')).filter(d => d !== runId && d.endsWith(`-${phase}`)).sort().pop();
let diff = '_No previous run._';
if (prev) {
  const old = Object.fromEntries(fs.readFileSync(R(`runs/${prev}/findings.jsonl`), 'utf8').trim().split('\n').map(l => JSON.parse(l)).map(f => [f.check_id, f.status]));
  const ch = findings.filter(f => old[f.check_id] && old[f.check_id] !== f.status).map(f => `- ${old[f.check_id] === 'PASS' ? '**REGRESSION** ' : ''}${f.check_id}: ${old[f.check_id]} -> ${f.status}`);
  diff = ch.length ? ch.join('\n') : `_No changes vs ${prev}._`;
}

const policyOrder = { auto: 0, ask: 1, never: 2 };
const fixes = findings.filter(f => ['FAIL', 'PARTIAL', 'ERROR', 'UNRUN'].includes(f.status)).sort((a, b) => a.tier - b.tier || policyOrder[a.fix_policy] - policyOrder[b.fix_policy]);
const md = `# Readiness report: ${runId}

**Verdict: ${verdict}**

Blocking T0: ${blocking.length} | Judgement-only T0 PASS: ${judgementOnly.length} | T1 gaps: ${t1gaps.length}

## Diff vs previous run
${diff}

## Findings
| Tier | ID | Status | Confidence | Fix policy | Evidence |
|---|---|---|---|---|---|
${findings.map(f => `| ${f.tier} | ${f.check_id} | ${f.status} | ${f.confidence} | ${f.fix_policy} | ${String(f.evidence).replace(/\|/g, '/').slice(0, 160)} |`).join('\n')}

## Fix list
${fixes.map((f, i) => `${i + 1}. \`${f.check_id}\` (${f.status}) - ${f.fix_policy === 'auto' ? 'fix phase may proceed' : f.fix_policy === 'ask' ? 'needs a yes' : 'human does it'}`).join('\n')}

## Memory proposals
See memory-proposals.md.
`;
fs.writeFileSync(path.join(runDir, 'report.md'), md);
// Memory proposals: derived from evidence only. Flag LESSONS lines that instruct skipping/passing checks that probes FAILED.
const proposals = [];
if (fs.existsSync(R('LESSONS.md'))) {
  for (const line of fs.readFileSync(R('LESSONS.md'), 'utf8').split('\n')) {
    if (!/skip|mark .*pass/i.test(line)) continue;
    const pats = [...line.matchAll(/T[0-2]-[A-Z]+(?:-[A-Z*]+)?/g)].map(m => new RegExp('^' + m[0].replace('*', '.*') + '$'));
    const contradicted = findings.filter(f => pats.some(re => re.test(f.check_id)) && ['FAIL', 'PARTIAL'].includes(f.status));
    if (contradicted.length) proposals.push(`- target: LESSONS.md\n  change: delete line: ${JSON.stringify(line.trim())}\n  source: ${contradicted.map(f => `probe:${f.check_id}@seq${f.trace_seq}`).join(', ')}\n  why: line instructs skipping/passing checks that deterministic probes FAIL; it is an instruction, not a lesson`);
  }
}
fs.writeFileSync(path.join(runDir, 'memory-proposals.md'), `# Memory proposals (${runId})\n\n${proposals.join('\n') || '_None._'}\n`);
console.log(JSON.stringify({ runId, verdict, runDir }));

function loadYaml(from) {
  for (const base of [path.join(from, 'package.json'), import.meta.url]) {
    try { return createRequire(base)('js-yaml'); } catch {}
  }
  console.error('js-yaml not found. Run `pnpm add -D js-yaml` in the target repo.'); process.exit(2);
}
