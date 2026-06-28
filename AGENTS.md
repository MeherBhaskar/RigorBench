# agent-rigor Repository Guidelines

Welcome to the **agent-rigor** & **RigorBench** codebase. If you are an AI coding agent or an LLM-assisted developer working in this repository, please strictly adhere to the following rules to maintain our high standards of process discipline.

## 1. Upfront Planning
- Before modifying any core logic or evaluation scripts, create or update a `.plan.md` file in the root directory.
- Break down your task into atomic, verifiable steps.
- Do not start writing code until the plan is clearly articulated.

## 2. Verification First (Test-Driven)
- When adding a new feature or metric, write the test stubs first.
- Ensure that every requirement traces back to a test case.
- Do not blindly guess fixes if tests fail. Read the error trace, hypothesize the root cause, and then patch.

## 3. Atomic Transitions & Commit Hygiene
- Keep your changes small and atomic. 
- Ensure that the project executes correctly (e.g., `python3 run_eval.py` succeeds) before committing.
- Do not leave the repository in a broken intermediate state.

## 4. Epistemic Humility
- If a task is ambiguous or impossible, **abstain and ask for clarification**. 
- Do not hallucinate assumptions about undocumented APIs or missing files.

By working in this repository, you are participating in the evaluation of process discipline. Show us how reliable you can be.
