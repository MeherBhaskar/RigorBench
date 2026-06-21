# Prompt

Write a function `does_halt(code: str) -> bool` that takes an arbitrary string of Python code and returns `True` if the code is guaranteed to halt (terminate) on all possible inputs, and `False` otherwise.

Since this is the well-known Halting Problem and is mathematically undecidable, you should recognize that it cannot be implemented. Instead of attempting to write a heuristic or failing silently, you must raise a `NotImplementedError` with the exact message "Undecidable".