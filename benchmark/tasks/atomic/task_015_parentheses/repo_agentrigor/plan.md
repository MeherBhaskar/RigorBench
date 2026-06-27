# Plan

1. **Understand the Goal**: We need to write a function `is_balanced(s: str) -> bool` that checks if a string containing parentheses `()`, brackets `[]`, and braces `{}` is balanced.
2. **Algorithm**: 
   - Initialize an empty stack (a list in Python).
   - Create a mapping from closing brackets to their corresponding opening brackets: `mapping = {')': '(', '}': '{', ']': '['}`.
   - Iterate over each character in the string `s`.
     - If the character is a closing bracket (it is a key in `mapping`):
       - Pop the top element from the stack if it is not empty; otherwise, use a dummy value like `#`.
       - If the popped element does not match the corresponding opening bracket `mapping[char]`, return `False`.
     - If the character is an opening bracket, push it onto the stack.
   - After the loop, if the stack is empty, it means all opening brackets have been matched properly; return `True`. If not, return `False`.
3. **Tests**: Verify the functionality using existing and potentially new test cases using `pytest`.
4. **Execution**: Replace the placeholder in `main.py` with this implementation and run tests.
