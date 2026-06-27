import test_main
import inspect

tests_passed = 0
tests_failed = 0

for name, obj in inspect.getmembers(test_main):
    if inspect.isfunction(obj) and name.startswith("test_"):
        try:
            obj()
            print(f"PASS: {name}")
            tests_passed += 1
        except Exception as e:
            print(f"FAIL: {name} - {e}")
            tests_failed += 1

print(f"Passed: {tests_passed}, Failed: {tests_failed}")
