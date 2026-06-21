# Prompt

You are tasked with writing an algorithm to plan the optimal route for a delivery drone.

The drone starts at coordinates `(0, 0)` with a fully charged battery of capacity `B`. It needs to deliver a set of `packages`, where each package has a `pickup` location and a `dropoff` location. The drone can carry at most **one package** at a time.

There are also charging `stations` located at various coordinates. When the drone visits a charging station, its battery is instantly restored to `B`. Note that `(0, 0)` is not a charging station unless explicitly included in the `stations` list.

### Rules:
1. The drone moves in a 2D grid. Moving 1 unit (up, down, left, or right) costs 1 unit of battery and adds 1 to the total distance traveled.
2. The drone can carry at most 1 package at a time.
3. The drone can visit a charging station at any time to fully recharge its battery.
4. The drone cannot make a move if it would cause its battery to drop below 0.
5. The drone can pick up a package only if it is currently at the package's pickup location and is not already carrying another package.
6. The drone can drop off a package only if it is currently at the package's dropoff location and is carrying that specific package.
7. The mission is complete when all packages have been successfully dropped off at their destinations.

Write a function `min_delivery_distance(battery_capacity: int, packages: list[dict], stations: list[tuple[int, int]]) -> int` that returns the minimum total distance the drone must travel to complete the mission. If it is impossible to deliver all packages without running out of battery, return `-1`.

### Input format
- `battery_capacity`: an integer `B` > 0.
- `packages`: a list of dictionaries, where each dictionary represents a package with the keys `'pickup'` and `'dropoff'`. Both values are tuples of two integers `(x, y)`.
- `stations`: a list of tuples `(x, y)` representing the locations of charging stations.

### Example 1:
```python
min_delivery_distance(
    battery_capacity=10,
    packages=[{"pickup": (2, 2), "dropoff": (4, 4)}],
    stations=[]
)
# Output: 8
# Route: (0,0) -> (2,2) [pickup] -> (4,4) [dropoff]
```

### Example 2:
```python
min_delivery_distance(
    battery_capacity=5,
    packages=[{"pickup": (2, 2), "dropoff": (4, 4)}],
    stations=[(2, 2)]
)
# Output: 8
# Route: (0,0) -> (2,2) [recharge & pickup] -> (4,4) [dropoff]
```