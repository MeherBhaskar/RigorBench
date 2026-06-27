from collections import deque

def plan_crafting(target: str, amount: int, recipes: dict[str, list[dict[str, int]]], inventory: dict[str, int]) -> list[tuple[str, int]] | None:
    if inventory.get(target, 0) >= amount:
        return []

    # Precompute useful items to prune irrelevant crafting actions
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

    def get_state(inv):
        return tuple(sorted((k, v) for k, v in inv.items() if v > 0))

    initial_state = get_state(inventory)
    queue = deque([(inventory.copy(), [])])
    visited = {initial_state}

    while queue:
        curr_inv, path = queue.popleft()

        for item, item_recipes in recipes.items():
            # Prune items that can never help craft the target
            if item not in useful_items:
                continue
                
            for r_idx, recipe in enumerate(item_recipes):
                can_craft = True
                for ing, req_qty in recipe.items():
                    if curr_inv.get(ing, 0) < req_qty:
                        can_craft = False
                        break
                
                if can_craft:
                    new_inv = curr_inv.copy()
                    for ing, req_qty in recipe.items():
                        new_inv[ing] -= req_qty
                    new_inv[item] = new_inv.get(item, 0) + 1
                    
                    if new_inv.get(target, 0) >= amount:
                        return path + [(item, r_idx)]
                        
                    new_state = get_state(new_inv)
                    if new_state not in visited:
                        visited.add(new_state)
                        queue.append((new_inv, path + [(item, r_idx)]))

    return None
