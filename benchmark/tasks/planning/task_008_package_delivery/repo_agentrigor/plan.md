# Plan for `plan_delivery_route`

## Problem Analysis
The task is to write a planning algorithm for a delivery robot on a 2D grid.
- `'S'` is the starting position.
- `'.'` is traversable space.
- `'X'` is an obstacle.
- `'A'`, `'B'`, `'C'`, etc. are packages.
The robot must collect all packages in strictly alphabetical order ('A' -> 'B' -> 'C' -> ...).
The robot can step on a package cell before it is time to collect it, but it is only collected when it is the next package in the sequence and the robot steps on it.
We must return the shortest sequence of moves (`"UP"`, `"DOWN"`, `"LEFT"`, `"RIGHT"`) to collect all packages, or `None` if no valid path exists.

## Mathematical & Algorithmic Optimizations
Since the collection order of packages is strictly fixed (from 'A' to the last package alphabetically), and the grid is static (obstacles do not change), the problem decomposes into independent shortest-path queries between consecutive targets:
1. Find position of `'S'` and all package characters.
2. Sort the package characters alphabetically. This gives us the target sequence: `S -> A -> B -> C -> ...`.
3. For each transition from $T_i$ to $T_{i+1}$:
   - Run a Breadth-First Search (BFS) to find the shortest path from $T_i$ to $T_{i+1}$.
   - All cells except `'X'` are considered traversable.
   - If any transition is impossible (BFS returns `None`), the entire route is impossible, so return `None`.
4. Concatenate the paths of all transitions and return the resulting list of moves.

### BFS Performance Optimization
Instead of copying the path at each step of the BFS queue (which is $O(L)$ per step, leading to $O(V \cdot L)$ time/space complexity), we will use a `parent` map to store the predecessor and the move for each visited cell.
Once the target is reached, we reconstruct the path in $O(L)$ time by backtracking from the target to the start, and then reversing the path. This keeps the BFS queue operations $O(1)$ and highly efficient.

## Edge Cases to Handle & Test
1. **No Packages**: If the grid contains only `'S'` and `'.'`/`'X'`, the robot has no packages to collect. The correct output is `[]`.
2. **Single Package**: A single package `'A'`.
3. **Unreachable Packages**: An obstacle completely blocks the path to one of the packages. The algorithm must return `None`.
4. **Passing Through Future Packages**: The shortest path to `'A'` requires passing through `'B'` or `'C'`. This is valid and must be supported.
5. **No Start Position**: If the grid does not contain `'S'`, we return `None`.
6. **Large Grid Performance**: A larger grid (e.g., $50 \times 50$) to verify that our optimized BFS runs extremely fast and does not time out.
7. **Complex Winding Path**: A maze-like grid where the robot must wind back and forth.

## Implementation & Verification Steps
1. **Write Plan**: (This file)
2. **Optimize BFS & Implement Algorithm**: Modify `main.py` to use the parent-pointer BFS and the full route planning logic.
3. **Expand Test Suite**: Add comprehensive test cases in `test_main.py` covering all the identified edge cases.
4. **Run Tests**: Execute `pytest` and verify all tests pass successfully.
