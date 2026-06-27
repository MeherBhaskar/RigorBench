import test_main
import types

success = True
for name in dir(test_main):
    if name.startswith('test_'):
        func = getattr(test_main, name)
        if isinstance(func, types.FunctionType):
            try:
                func()
                print(f"{name}: PASS")
            except Exception as e:
                print(f"{name}: FAIL")
                print(e)
                success = False

if not success:
    exit(1)
else:
    print("ALL PASSED")
