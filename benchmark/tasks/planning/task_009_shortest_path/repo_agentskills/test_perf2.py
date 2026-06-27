import time
from main import plan_crafting

def test_perf2():
    recipes = {
        "Target": [{"A": 1}],
        "A": [{"B": 1}],
        "B": [{"C": 1}],
    }
    # Add many useless recipes
    for i in range(20):
        recipes[f"Useless_{i}"] = [{"Base": 1}]
        
    inventory = {"C": 1, "Base": 20}
    
    start = time.time()
    plan = plan_crafting("Target", 1, recipes, inventory)
    end = time.time()
    print(f"Time: {end - start}s")
    assert plan is not None

if __name__ == "__main__":
    test_perf2()
