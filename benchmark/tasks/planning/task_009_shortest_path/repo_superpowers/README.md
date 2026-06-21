# Prompt

You are given a crafting system where items can be created using specific recipes. Some items have multiple different recipes. You need to find the **shortest possible sequence** of crafting actions to obtain a certain amount of a target item, starting from a given inventory.

Write a function `plan_crafting(target: str, amount: int, recipes: dict[str, list[dict[str, int]]], inventory: dict[str, int]) -> list[tuple[str, int]] | None`

**Inputs:**
- `target`: The name of the item you want to obtain.
- `amount`: The total quantity of the target item you need to have in your inventory.
- `recipes`: A dictionary where keys are item names and values are lists of recipes. Each recipe is a dictionary mapping ingredient names to required quantities to produce **exactly 1 unit** of the item. Every recipe requires at least one ingredient.
- `inventory`: A dictionary representing the items you currently have and their quantities. Items not listed have a quantity of 0.

**Output:**
- Return a list of tuples `(item_name, recipe_index)` representing the sequence of crafting actions.
- Each action crafts exactly 1 unit of `item_name` using the recipe at `recipes[item_name][recipe_index]`.
- The sequence must be valid (you must have the required ingredients in your inventory before each crafting step).
- The sequence must be the **shortest possible**. If there are multiple valid sequences of the same shortest length, you can return any of them.
- If it's already satisfied (you have `amount` of `target` in inventory), return an empty list `[]`.
- If it's impossible to craft the target amount, return `None`.

**Example:**
```python
recipes = {
    "A": [
        {"B": 1, "C": 1},
        {"D": 2}
    ],
    "B": [
        {"C": 1}
    ]
}
inventory = {"C": 2, "D": 2}

# To get 1 "A":
# Option 1: Craft "B" using recipe 0, then "A" using recipe 0. Length: 2 actions.
# Option 2: Craft "A" using recipe 1 (needs 2 "D"). Length: 1 action.

# The shortest sequence is Option 2.
plan_crafting("A", 1, recipes, inventory) # Returns [("A", 1)]
```