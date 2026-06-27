from main import plan_crafting
import time

recipes = {
    "Target": [{"A": 1}],
    "A": [{"B": 1}],
    "B": [{"C": 1}],
    "C": [{"Start": 1}]
}

# add irrelevant items
for i in range(100):
    recipes[f"Irrelevant_{i}"] = [{"Start": 1}]
    recipes[f"Irrelevant_{i}_2"] = [{f"Irrelevant_{i}": 1}]

inventory = {"Start": 100}

start = time.time()
plan = plan_crafting("Target", 1, recipes, inventory)
end = time.time()
print(f"Time: {end-start}, Path length: {len(plan) if plan else 'None'}")
