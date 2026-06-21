# Prompt

You are tasked with writing a planning algorithm for a delivery robot. The robot operates on a 2D grid.

The grid is represented as a list of strings where:
- `'S'` is the starting position of the robot.
- `'.'` is an empty space the robot can move to.
- `'X'` is an obstacle the robot cannot pass through.
- `'A'`, `'B'`, `'C'`, etc. are packages that the robot must collect.

The robot must collect all packages in strictly alphabetical order (first 'A', then 'B', then 'C', etc.).
The robot can move up, down, left, or right. Each move takes 1 step. You can step on a package cell before it's time to collect it, but it will only be collected when it's the correct next package in the sequence and the robot steps on it.

Implement the function `plan_delivery_route(grid: list[str]) -> list[str]` which returns the shortest sequence of moves to collect all packages in the correct order. The moves should be represented as a list of strings: `"UP"`, `"DOWN"`, `"LEFT"`, `"RIGHT"`.
If there is no valid path to collect all packages, return `None`.

Example:
grid = [
  "S..",
  "XX.",
  "B.A"
]
Returns: `["RIGHT", "RIGHT", "DOWN", "DOWN", "LEFT", "LEFT"]`

Explanation: The robot starts at (0,0), goes right twice to (0,2), down twice to (2,2) to pick up 'A', then left twice to (2,0) to pick up 'B'.
