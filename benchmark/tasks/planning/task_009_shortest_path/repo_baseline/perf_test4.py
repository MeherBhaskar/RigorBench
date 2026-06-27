from main import plan_crafting
import time

recipes = {
    "Sword": [{"Blade": 1}],
    "Blade": [{"Iron": 1}],
    "Iron": [{"Ore": 1}]
}
inventory = {"Ore": 1000}

start = time.time()
plan = plan_crafting("Sword", 100, recipes, inventory)
end = time.time()
print(f"Time: {end-start}, Path length: {len(plan) if plan else 'None'}")
