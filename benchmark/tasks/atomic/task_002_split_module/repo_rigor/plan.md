# Plan

1. **Create submodules**: Create three new files (`user.py`, `order.py`, `payment.py`) and move the respective classes (`User`, `Order`, `Payment`) from `monolith.py` into them.
2. **Update monolith**: Modify `monolith.py` to import `User`, `Order`, `Payment` from the newly created submodules. This ensures backwards compatibility so any existing code importing from `monolith.py` continues to work.
3. **Write tests**: Update `test.py` to add tests that verify the classes can be imported from both the submodules and the `monolith` module.
4. **Verify tests**: Run the tests using `pytest` to ensure everything works correctly.
