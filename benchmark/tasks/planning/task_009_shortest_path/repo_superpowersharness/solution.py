import heapq
from typing import Dict, List, Tuple

def plan_crafting(target: str, amount: int, recipes: Dict[str, List[Dict[str, int]]], inventory: Dict[str, int]) -> List[Tuple[str, int]] | None:
    if inventory.get(target, 0) >= amount:
        return []

    # 1. Compute useful items using backward propagation
    useful_items = {target}
    changed = True
    while changed:
        changed = False
        for item, item_recipes in recipes.items():
            if item in useful_items:
                for recipe in item_recipes:
                    for ing in recipe:
                        if ing not in useful_items:
                            useful_items.add(ing)
                            changed = True

    # 2. Compute producible items using forward propagation
    producible = set(inventory.keys())
    changed = True
    while changed:
        changed = False
        for item, item_recipes in recipes.items():
            if item not in producible:
                for recipe in item_recipes:
                    if all(ing in producible for ing in recipe):
                        producible.add(item)
                        changed = True
                        break

    # If target is not producible, it's impossible
    if target not in producible:
        return None

    # Filter inventory to only keep useful items
    filtered_inventory = {k: v for k, v in inventory.items() if k in useful_items and v > 0}

    # Helper functions for state conversion
    def to_tuple(d: dict[str, int]) -> tuple[tuple[str, int], ...]:
        return tuple(sorted((k, v) for k, v in d.items() if v > 0))

    def simplify(req: dict[str, int], inv: dict[str, int]) -> tuple[dict[str, int], dict[str, int]]:
        new_req = {}
        new_inv = inv.copy()
        for item, qty in req.items():
            inv_qty = new_inv.get(item, 0)
            if inv_qty > 0:
                match_qty = min(qty, inv_qty)
                new_inv[item] -= match_qty
                if new_inv[item] == 0:
                    del new_inv[item]
                rem_qty = qty - match_qty
                if rem_qty > 0:
                    new_req[item] = rem_qty
            else:
                new_req[item] = qty
        return new_req, new_inv

    # Dijkstra setup
    init_req, init_inv = simplify({target: amount}, filtered_inventory)
    init_state = (to_tuple(init_req), to_tuple(init_inv))
    
    pq = [(0, init_state, [])]
    visited = {init_state}

    while pq:
        cost, state, path = heapq.heappop(pq)

        req_tuple, inv_tuple = state
        if not req_tuple:
            # Found shortest path!
            return path[::-1]

        # Convert back to dicts for manipulation
        req = dict(req_tuple)
        inv = dict(inv_tuple)

        # Pruning check 1: sum of requirements vs sum of remaining inventory
        # Since R - I can never decrease, we can prune if R > I.
        sum_req = sum(req.values())
        sum_inv = sum(inv.values())
        if sum_req > sum_inv:
            continue

        # Deterministically choose one requirement to expand
        # Sorting the keys to ensure order independence and canonical states
        focus_item = sorted(req.keys())[0]

        # We need to resolve 1 unit of focus_item
        # Option: Craft it using one of its recipes
        # Note: We don't have option to match it since simplify() already matched everything possible
        focus_recipes = recipes.get(focus_item, [])
        for r_idx, recipe in enumerate(focus_recipes):
            # Pruning check: all ingredients must be producible
            # (If not, we can never satisfy them)
            if not all(ing in producible for ing in recipe):
                continue

            # Create new requirements: decrement focus_item by 1, add recipe ingredients
            new_req = req.copy()
            new_req[focus_item] -= 1
            if new_req[focus_item] == 0:
                del new_req[focus_item]

            for ing, qty in recipe.items():
                new_req[ing] = new_req.get(ing, 0) + qty

            # Simplify the new state
            sim_req, sim_inv = simplify(new_req, inv)
            
            # Additional pruning: check if any required item is not producible
            if any(k not in producible for k in sim_req):
                continue

            new_state = (to_tuple(sim_req), to_tuple(sim_inv))
            if new_state not in visited:
                visited.add(new_state)
                heapq.heappush(pq, (cost + 1, new_state, path + [(focus_item, r_idx)]))

    return None
