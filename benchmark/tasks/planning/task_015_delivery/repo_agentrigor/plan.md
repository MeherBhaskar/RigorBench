# Plan: Optimal Route Planning for Delivery Drone

## 1. Problem Analysis
The problem asks us to find the minimum total Manhattan distance for a drone starting at `(0, 0)` to deliver a set of packages under a battery capacity constraint `B`.
- **Drone Capacity**: Maximum 1 package at a time.
- **Battery Constraint**: Every unit of movement costs 1 battery and adds 1 to distance. Battery cannot drop below 0.
- **Charging Stations**: Instantly restores battery to `B`.
- **Mission Completion**: All packages delivered.

## 2. State Space and Representation
Since the drone moves in an empty 2D grid, the shortest path between any two points of interest (POIs) is the Manhattan distance. The drone only needs to visit POIs (start, pickups, dropoffs, and stations). Stopping at any other point is suboptimal by the triangle inequality.

We represent the state of the drone as a tuple `(u, delivered, carried)` where:
- `u`: Index of the current coordinate in the list of unique POI coordinates.
- `delivered`: A bitmask of delivered packages (integer, length `N` where `N = len(packages)`).
- `carried`: The index of the package currently being carried, or `-1` if none.

We also track:
- `dist`: The total distance traveled so far (our primary optimization objective).
- `bat`: The remaining battery.

## 3. Dijkstra's Search Algorithm
We will use Dijkstra's algorithm to find the minimum distance to reach a state where all packages are delivered.
The priority queue `pq` will store tuples of `(dist, -bat, u, delivered, carried)`. We store `-bat` to prioritize states with more battery when distances are equal.

### Pareto Dominance and Pruning
A state $A$ dominates state $B$ if:
1. $A.\text{dist} \le B.\text{dist}$
2. $A.\text{bat} \ge B.\text{bat}$
3. $A.\text{state\_key} = B.\text{state\_key}$

Since Dijkstra's algorithm pops states in non-decreasing order of `dist`, any state popped from the queue has a distance greater than or equal to all previously popped states.
Thus, when we pop a state `(u, delivered, carried)` with battery `bat`:
- If `bat <= max_battery_seen[(u, delivered, carried)]`, then this state is dominated by a previously popped state (which had smaller/equal distance and larger/equal battery) and can be safely pruned.
- Otherwise, this state is not dominated. We update `max_battery_seen[(u, delivered, carried)] = bat` and proceed to expand it.

We can also apply this pruning check at push-time to avoid unnecessary queue insertions.

## 4. State Transitions
To optimize search efficiency, we separate **movement** transitions from **free action** transitions.

### 4.1 Free Actions (Cost 0, Distance 0)
When at coordinate `u`:
1. **Pickup**: If `carried == -1`, for any package `i` that is not yet delivered and whose pickup is at `u`:
   - Transition to `(u, delivered, i)` with same `dist` and `bat`.
2. **Dropoff**: If `carried != -1` and `u` is the dropoff location of package `carried`:
   - Transition to `(u, delivered | (1 << carried), -1)` with same `dist` and `bat`.

### 4.2 Movement Transitions
Instead of transitioning to *all* coordinates in the grid, we only transition to a minimal set of useful candidate coordinates `v`:
- All charging stations in `stations`.
- If `carried == -1`: the pickup coordinate of any undelivered package.
- If `carried != -1`: the dropoff coordinate of the carried package.

For each candidate coordinate `v` (where `v != u`):
- Calculate Manhattan distance `cost = abs(ux - vx) + abs(uy - vy)`.
- If `bat >= cost`, we can move to `v`.
- The new battery is `next_bat = bat - cost`.
- If `v` is a charging station, `next_bat = B`.
- Push state `(v, delivered, carried)` to `pq` with distance `dist + cost` and battery `next_bat`.

## 5. Correctness Proof of Candidate Pruning
Why is it sufficient to only consider stations, undelivered pickups (when carrying nothing), and the active dropoff (when carrying a package) as movement destinations?
- By the triangle inequality of Manhattan distance, `dist(u, v) + dist(v, w) >= dist(u, w)`.
- If we move to any other coordinate `v` without performing an action (pickup, dropoff, or recharge) at `v`, the path `u -> v -> w` will have a larger or equal distance and a smaller or equal battery than the direct path `u -> w`.
- Therefore, visiting any coordinate `v` is only useful if we perform a state-changing action at `v` immediately upon arrival.
- The only useful actions are recharging (at stations), picking up (at undelivered pickups when carrying nothing), and dropping off (at the dropoff of the carried package).
- Thus, restricting movement targets to this candidate set is mathematically complete and optimal.
