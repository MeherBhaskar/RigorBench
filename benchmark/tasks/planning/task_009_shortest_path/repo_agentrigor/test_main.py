import pytest
from main import plan_crafting

def verify_plan(target, amount, recipes, inventory, plan):
    if plan is None:
        return False
    inv = inventory.copy()
    for item, r_idx in plan:
        recipe = recipes[item][r_idx]
        for ing, req in recipe.items():
            if inv.get(ing, 0) < req:
                return False
            inv[ing] -= req
        inv[item] = inv.get(item, 0) + 1
    return inv.get(target, 0) >= amount

def test_already_satisfied():
    recipes = {"A": [{"B": 1}]}
    inventory = {"A": 2}
    assert plan_crafting("A", 1, recipes, inventory) == []

def test_simple_crafting():
    recipes = {"A": [{"B": 1, "C": 1}]}
    inventory = {"B": 1, "C": 1}
    plan = plan_crafting("A", 1, recipes, inventory)
    assert plan == [("A", 0)]

def test_shortest_path():
    recipes = {
        "A": [{"B": 1, "C": 1}, {"D": 2}],
        "B": [{"C": 1}]
    }
    inventory = {"C": 2, "D": 2}
    plan = plan_crafting("A", 1, recipes, inventory)
    assert plan == [("A", 1)]

def test_impossible():
    recipes = {
        "A": [{"B": 1}]
    }
    inventory = {"C": 1}
    assert plan_crafting("A", 1, recipes, inventory) is None

def test_multi_step():
    recipes = {
        "Sword": [{"Blade": 1, "Hilt": 1}],
        "Blade": [{"Iron": 2}],
        "Hilt": [{"Wood": 1}]
    }
    inventory = {"Iron": 4, "Wood": 2}
    plan = plan_crafting("Sword", 2, recipes, inventory)
    assert plan is not None
    assert len(plan) == 6
    assert verify_plan("Sword", 2, recipes, inventory, plan)

def test_complex_choice():
    recipes = {
        "X": [{"Y": 1}, {"Z": 1}],
        "Y": [{"A": 1, "B": 1}],
        "Z": [{"C": 1}],
        "C": [{"D": 1}]
    }
    inventory = {"A": 1, "B": 1, "D": 1}
    plan = plan_crafting("X", 1, recipes, inventory)
    assert plan is not None
    assert len(plan) == 2
    assert verify_plan("X", 1, recipes, inventory, plan)

def test_cyclic_recipes():
    recipes = {
        "A": [{"B": 1}],
        "B": [{"A": 1}]
    }
    inventory = {"A": 1}
    plan = plan_crafting("B", 1, recipes, inventory)
    assert plan == [("B", 0)]

    inventory = {}
    plan = plan_crafting("B", 1, recipes, inventory)
    assert plan is None

def test_unrelated_recipes_pruning():
    recipes = {
        "A": [{"B": 1, "C": 1}],
        "X": [{"Y": 1}],
        "Y": [{"Z": 1}],
        "Z": [{"W": 1}],
    }
    inventory = {
        "B": 1,
        "C": 1,
        "Y": 1000,
        "Z": 1000,
        "W": 1000,
    }
    plan = plan_crafting("A", 1, recipes, inventory)
    assert plan == [("A", 0)]

def test_impossible_due_to_unproducible():
    recipes = {
        "A": [{"B": 1, "C": 1}],
        "B": [{"D": 1}]
    }
    inventory = {"D": 1}
    plan = plan_crafting("A", 1, recipes, inventory)
    assert plan is None

def test_multiple_amounts():
    recipes = {
        "A": [{"B": 1}],
        "B": [{"C": 1}]
    }
    inventory = {"C": 5}
    plan = plan_crafting("A", 3, recipes, inventory)
    assert plan is not None
    assert len(plan) == 6
    assert verify_plan("A", 3, recipes, inventory, plan)
