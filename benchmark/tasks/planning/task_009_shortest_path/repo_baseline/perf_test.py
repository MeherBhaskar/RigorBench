from main import plan_crafting
import time

recipes = {
    "Sword": [{"Blade": 1, "Hilt": 1}],
    "Blade": [{"Iron": 2}],
    "Hilt": [{"Wood": 1}],
    "Iron": [{"Ore": 1, "Coal": 1}],
    "Wood": [{"Branch": 2}],
    "Branch": [{"Twig": 2}]
}
inventory = {"Ore": 100, "Coal": 100, "Twig": 100}

start = time.time()
plan = plan_crafting("Sword", 1, recipes, inventory)
end = time.time()
print(f"Time: {end-start}, Path length: {len(plan) if plan else 'None'}")
