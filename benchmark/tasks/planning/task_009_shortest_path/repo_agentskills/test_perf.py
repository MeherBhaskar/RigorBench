import time
from main import plan_crafting

def test_perf():
    recipes = {f"Item_{i}": [{f"Item_{i-1}": 1}] for i in range(1, 20)}
    inventory = {"Item_0": 1}
    
    start = time.time()
    plan = plan_crafting("Item_19", 1, recipes, inventory)
    end = time.time()
    print(f"Time: {end - start}s")
    assert plan is not None

if __name__ == "__main__":
    test_perf()
