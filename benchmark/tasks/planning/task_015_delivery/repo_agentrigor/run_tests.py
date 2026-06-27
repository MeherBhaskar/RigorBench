import test_main

for name, func in list(test_main.__dict__.items()):
    if name.startswith("test_") and callable(func):
        print(f"Running {name}...")
        func()
print("All tests passed!")

