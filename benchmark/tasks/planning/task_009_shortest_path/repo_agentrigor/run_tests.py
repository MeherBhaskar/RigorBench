import test_main

# Discover all test functions in test_main starting with 'test_'
tests = [
    getattr(test_main, name)
    for name in dir(test_main)
    if name.startswith("test_") and callable(getattr(test_main, name))
]

for t in tests:
    try:
        t()
        print(f"{t.__name__} passed")
    except AssertionError as e:
        print(f"{t.__name__} failed")
        raise e
