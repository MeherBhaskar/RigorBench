# Prompt

You are tasked with planning a delivery route for a robot navigating a 2D grid. The grid contains empty spaces (`0`) and obstacles (`1`). The robot starts at a given `start` coordinate and must visit a list of `waypoints`. The robot can move horizontally or vertically to adjacent empty cells (1 step per move).

Write a function `plan_delivery_route(grid, start, waypoints)` that returns the **minimum number of steps** required to visit all waypoints starting from the `start` position. The waypoints can be visited in any order. 

If it is impossible to visit all waypoints due to obstacles, return `-1`.

### Inputs:
- `grid`: A 2D list of integers, where `0` represents an empty space and `1` represents an obstacle. (Dimensions up to 15x15)
- `start`: A tuple `(r, c)` representing the starting row and column of the robot.
- `waypoints`: A list of tuples `[(r1, c1), (r2, c2), ...]`, representing the coordinates of the waypoints to visit. There will be at most 8 waypoints.

### Output:
- An integer representing the minimum number of steps to visit all waypoints, or `-1` if unreachable.

### Example
```python
grid = [
    [0, 0, 0],
    [0, 1, 0],
    [0, 0, 0]
]
start = (1, 0)
waypoints = [(1, 2), (0, 0)]
```
Visiting `(0, 0)` first takes 1 step. From `(0, 0)`, visiting `(1, 2)` takes 3 steps. Total = 4. Returning 4.