# agent-rigor & RigorBench

Your AI coding agent passes the tests. But did it plan first? Add a regression test? Avoid the doom loop? **agent-rigor** enforces the six-phase discipline lifecycle that separates reliable agents from lucky ones.

![Agent-Rigor Demo](figures/demo.gif)
*(Above: A comparison of standard ReAct trial-and-error vs. Agent-Rigor's structured execution.)*

## The Impact

We benchmarked Agent-Rigor across 100 complex software tasks using our companion evaluation suite, **RigorBench**. Enforcing process discipline fundamentally raises the capability ceiling of your AI.

| Metric | Baseline ReAct | agent-rigor | Impact |
|--------|----------------|-------------|--------|
| **Process Quality** | 0.29 | 0.52 | **+79% Improvement** |
| **Outcome Correctness** | 64% | 83% | **+30% Improvement** |

## Quick Start (under 60 seconds)

You can wire `agent-rigor` into your existing AI coding assistant in seconds.

```bash
pip install agent-rigor
# Wrap your favorite agent to enforce the 6-phase lifecycle
agent-rigor wrap claude-code
```

## Why this exists

Consider two agents solving the same bug. Agent A formulates a hypothesis, writes a targeted fix, adds a regression test, and verifies it passes. Agent B tries five random patches in sequence until it stumbles upon one that makes the tests pass, without understanding why or adding tests. Under existing benchmarks, both get a perfect score. Yet Agent A is reliable and safe for production, while Agent B is a fragile liability. **agent-rigor** exists to force your AI to act like Agent A, and **RigorBench** exists to measure it.

---

## Live RigorScore Leaderboard

This leaderboard tracks the process discipline of leading foundational agents and harnesses on the RigorBench suite. (Higher is better, scaled `[0, 1]`)

| Rank | Agent / Harness | RigorScore | Outcome Score | Notes |
|------|-----------------|------------|---------------|-------|
| 1 | **agent-rigor (Gemini 3.5 Flash)** | **0.52** | **83%** | Upfront planning enforced |
| 2 | Superpowers (Gemini 3.5 Flash) | 0.35 | 70% | High iterative iteration |
| 3 | Agent-Skills (Gemini 3.5 Flash) | 0.30 | 72% | Excellent Clarification |
| 4 | Baseline ReAct (Gemini 3.5 Flash) | 0.29 | 64% | Zero-shot standard |

*Want to add your agent? Open a PR with your trajectory logs!*

---

## Compatibility Matrix

`agent-rigor` acts as an intercepting harness. Here is what it works with out of the box:

| Agent / Harness | Compatibility | Notes |
|-----------------|---------------|-------|
| **Claude Code** | ✅ Full | Natively supports custom rules and lifecycle hooks |
| **Cursor** | ✅ Full | Enforced via `.cursorrules` and workspace sync |
| **Gemini CLI** | ✅ Full | Natively wraps the execution loop |
| **Aider** | 🚧 Partial | Custom architect mode required |
| **Codex CLI** | ❌ Planned | Support coming in v1.2 |

---

## Citation

If you use RigorBench or agent-rigor in your research, please cite our paper:

```bibtex
@inproceedings{bhaskar2026rigorbench,
  title={RigorBench: Measuring Process Discipline in AI Coding Agents},
  author={Bhaskar, Meher and others},
  booktitle={Proceedings of the International Conference on Software Engineering (ICSE)},
  year={2026}
}
```
