# RigorBench: A Benchmark for Process Discipline in AI Coding Agents

This repository contains the source code, evaluation datasets, and analysis scripts for **RigorBench**, the first benchmark designed to measure *process discipline* in AI coding agents. 

While existing benchmarks evaluate agents almost exclusively on outcome correctness (whether the generated code passes tests), RigorBench evaluates the behavioral process of agents across nine distinct dimensions.

---

## Repository Structure

```
├── benchmark/
│   ├── rigorbench/          # Core Python library containing trajectory models and scorers
│   ├── results/              # Checked-in raw evaluation results (YAML files) for 400+ runs
│   ├── tasks/                # Curation of 100 benchmark tasks across 5 categories
│   ├── compute_extended.py   # Computes trajectory and repository-based process metrics
│   ├── compute_sc.py         # Specification Coverage scorer using LLM-as-judge
│   ├── compute_cbs.py        # Clarification Behavior Score evaluator
│   └── generate_final_table.py
├── paper/
│   └── rigorbench.tex        # LaTeX source code for the publication
└── run_eval.py               # Master reproduction script (aggregates all 9 metrics)
```

---

## Getting Started

### 1. Installation

RigorBench requires Python 3.10+ and a few lightweight dependencies for static analysis and parsing.

```bash
# Clone the repository
git clone https://github.com/MeherBhaskar/RigorBench.git
cd RigorBench

# Install dependencies
pip install pyyaml pyflakes
```

### 2. Reproducing the Evaluation Tables

To reproduce the exact 9-metric process evaluation table and LaTeX snippets reported in the paper, run the master evaluation entrypoint from the repository root:

```bash
python3 run_eval.py
```

This will parse the 400+ checked-in trajectories and repository artifacts, calculate the metrics, and print both a Markdown table and a LaTeX snippet matching the publication.

---

## Evaluated Process Metrics

RigorBench evaluates coding agents across nine process dimensions, all scaled from `[0, 1]` where **higher is better** ($\uparrow$):

1. **RigorScore (Composite)**: The weighted average of the core process pillars.
2. **Regression Resilience (RR) $\uparrow$**: Measures development stability. Defined as $1 - \text{Regression Ratio}$, where a regression is a transition from a passing test suite state to a failing test suite state.
3. **Exploration Efficiency (EE) $\uparrow$**: Measures how targeted the agent's file access is. Ratio of modified files to total read/modified files.
4. **Test Assertion Density (TAD) $\uparrow$**: Evaluates test quality. Measures the average number of meaningful assertions per test function (excluding trivial checks like `assert True`).
5. **Dead Code Avoidance (DCA) $\uparrow$**: Measures code cleanliness. Ratio of active, used symbols to total declared symbols.
6. **Diff Minimality (DM) $\uparrow$**: Measures edit surgical precision. Penalizes excessive code churn.
7. **Contextual Grounding Rate (CGR) $\uparrow$**: Measures grounding of imports. Ratio of valid imports (stdlib, local files, requirements) to total imports.
8. **Specification Coverage (SC) $\uparrow$**: Evaluates semantic completeness against the task README using an LLM-as-judge.
9. **Clarification Behavior Score (CBS) $\uparrow$**: Evaluates whether the agent asks clarifying questions when given an ambiguous task.

---

## Citation

If you use RigorBench in your research, please cite our work:

```bibtex
@inproceedings{bhaskar2026rigorbench,
  title={RigorBench: Measuring Process Discipline in AI Coding Agents},
  author={Bhaskar, Meher and others},
  booktitle={Proceedings of the International Conference on Software Engineering (ICSE)},
  year={2026}
}
```
