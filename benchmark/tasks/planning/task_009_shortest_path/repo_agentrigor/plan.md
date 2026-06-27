# Plan - Shortest Path Crafting Planner

## 1. Requirements Analysis
We need to find the shortest sequence of crafting actions to obtain `amount` of a `target` item starting from an initial `inventory`.
- Inputs:
  - `target` (str): Item to obtain.
  - `amount` (int): Required quantity of target.
  - `recipes` (dict[str, list[dict[str, int]]]): Dictionary mapping items to their recipe variations (each producing 1 unit).
  - `inventory` (dict[str, int]): Initial quantities of items.
- Output:
  - A list of `(item_name, recipe_index)` tuples representing the shortest path of actions, or `None` if impossible, or `[]` if already satisfied.

## 2. Optimization Strategies
A simple BFS can suffer from state space explosion due to unrelated items and impossible recipe branches. We will implement three optimization layers:

1. **Producibility Analysis**:
   - Compute the set of all items that can be produced starting from the initial inventory.
   - If the `target` is not producible, return `None` immediately.
   - Filter recipes: remove any recipe that requires an ingredient that is not producible.

2. **Reachability (Useful Set) Analysis**:
   - Determine the transitive ingredients required to craft the `target` using backward reachability from `target`.
   - Any item not in this "useful" set can be ignored.
   - Filter the initial inventory to only include items in the useful set.
   - Filter the recipes to only include items/recipes in the useful set.

3. **Optimized BFS Search**:
   - Use BFS to guarantee finding the shortest path first.
   - State representation: sorted tuple of `(item, qty)` for items in the useful set with `qty > 0`.
   - Keep track of `visited` states to avoid cycles.

## 3. Test Plan
We will run the existing tests using `poetry run pytest test_main.py` and write additional tests for:
- Cyclic dependencies (e.g., A -> B -> A)
- Impossible targets due to unproducible ingredients
- Multiple recipes with different lengths and resource constraints
- Filtering of unrelated items from inventory and recipes
