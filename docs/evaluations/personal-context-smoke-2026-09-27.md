# Personal-context cross-harness smoke check

Date: 2026-09-27

This smoke check validates discovery and a few key behaviors. It does not prove
the skill improves outcomes over a no-skill baseline.

## Setup

- Harnesses: agy 1.2.11 and Kiro CLI 2.10.0.
- Model labels requested: `claude-sonnet-4-6` in agy and `claude-sonnet-4.6` in Kiro.
- Fixture: synthetic context with preferred language Rust, local tools, and no
  database preference.
- No private profile files were used for the counted scenarios.

## Results

| Scenario | agy | Kiro | Expected behavior |
|----------|-----|------|-------------------|
| Read synthetic context file | Pass: answered `Rust` | Pass: read the fixture file and answered `Rust` | Use the supplied fact only |
| Apply technical-prose rule | Pass: withheld a formal dictionary verdict and suggested `use` | Partial: withheld the verdict, but added an unsupported claim about the dictionary's status | Do not invent claims beyond the reference |
| Load technical-prose reference | Pass: stated the Issue 9 PDF condition and named prohibited invented claims | Pass with `--trust-tools=fs_read`: read the skill and reference, then stated both rules | Follow the linked reference |
| Unrelated arithmetic | Pass: `56` | Pass: `56` | Answer directly without personal context |

Kiro could not read the technical-prose reference without trusted file-read
access. Passing `--trust-tools=fs_read` let it read both the skill and the
reference. Kiro also reported that some MCP servers did not load during these
noninteractive runs.

An earlier environment-variable-only fixture attempt returned an answer based
on unrelated context. I excluded it. The counted file case named the synthetic
fixture path directly and instructed both harnesses to read only that file.

## Limits and next run

- This was a small smoke check, not a paired with-skill versus without-skill
  evaluation.
- The requested model labels differ by harness. Do not compare response quality
  as if the model route were identical.
- Next, run all five starter scenarios from `../skill-evaluation.md` with and
  without the skill in each harness. Keep the fixture and scoring blind.
