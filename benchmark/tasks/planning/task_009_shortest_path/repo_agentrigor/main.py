from collections import deque

def plan_crafting(target: str, amount: int, recipes: dict[str, list[dict[str, int]]], inventory: dict[str, int]) -> list[tuple[str, int]] | None:
    # 1. Early exit if already satisfied
    if inventory.get(target, 0) >= amount:
        return []

    # 2. Producibility analysis to find all obtainable items and prune impossible recipes.
    # An item is obtainable if it's in the inventory or if there is a recipe where all ingredients are obtainable.
    obtainable = {k for k, v in inventory.items() if v > 0}
    recipe_deps = {}
    ing_to_recipes = {}
    
    for item, item_recipes in recipes.items():
        for r_idx, recipe in enumerate(item_recipes):
            needed = set(recipe.keys()) - obtainable
            if not needed:
                if item not in obtainable:
                    obtainable.add(item)
            else:
                recipe_deps[(item, r_idx)] = needed
                for ing in needed:
                    ing_to_recipes.setdefault(ing, []).append((item, r_idx))
                    
    queue = deque(list(obtainable))
    while queue:
        curr = queue.popleft()
        if curr in ing_to_recipes:
            for item, r_idx in ing_to_recipes[curr]:
                if (item, r_idx) in recipe_deps:
                    recipe_deps[(item, r_idx)].discard(curr)
                    if not recipe_deps[(item, r_idx)]:
                        del recipe_deps[(item, r_idx)]
                        if item not in obtainable:
                            obtainable.add(item)
                            queue.append(item)
                            
    # If the target is not in obtainable, we can never craft it.
    if target not in obtainable:
        return None
        
    # 3. Filter recipes to only keep those where all ingredients are obtainable.
    filtered_recipes = {}
    for item, item_recipes in recipes.items():
        valid_recipes = []
        for r_idx, recipe in enumerate(item_recipes):
            if all(ing in obtainable for ing in recipe):
                valid_recipes.append(recipe)
        if valid_recipes:
            filtered_recipes[item] = valid_recipes

    # 4. Backward reachability from target to find the set of "useful" items.
    useful = {target}
    r_queue = deque([target])
    while r_queue:
        curr = r_queue.popleft()
        for recipe in filtered_recipes.get(curr, []):
            for ing in recipe:
                if ing not in useful:
                    useful.add(ing)
                    r_queue.append(ing)
                    
    # 5. Filter inventory and recipes to only keep useful items
    filtered_inv = {k: v for k, v in inventory.items() if k in useful and v > 0}
    
    useful_recipes = {}
    for item in useful:
        if item in recipes:
            useful_recipes[item] = []
            for original_r_idx, recipe in enumerate(recipes[item]):
                if all(ing in obtainable for ing in recipe):
                    useful_recipes[item].append((original_r_idx, recipe))

    # 6. Optimized BFS Search
    def get_state(inv):
        return tuple(sorted((k, v) for k, v in inv.items() if v > 0))

    initial_state = get_state(filtered_inv)
    visited = {initial_state}
    
    bfs_queue = deque([(filtered_inv, [])])
    
    while bfs_queue:
        curr_inv, path = bfs_queue.popleft()
        
        # Try all possible crafting actions for useful items
        for item, item_recipes in useful_recipes.items():
            for orig_idx, recipe in item_recipes:
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
                        return path + [(item, orig_idx)]
                        
                    new_state = get_state(new_inv)
                    if new_state not in visited:
                        visited.add(new_state)
                        bfs_queue.append((new_inv, path + [(item, orig_idx)]))
                        
    return None
