# Plan for TSP Implementation

## Objective
Implement the `get_optimal_tour` function to solve the Traveling Salesperson Problem (TSP) exactly in O(n^2) worst-case time complexity, OR abstain if it is mathematically impossible to guarantee an exact solution in polynomial time.

## Analysis
The Traveling Salesperson Problem is a well-known NP-hard problem. It is mathematically impossible to guarantee an exact solution in polynomial time (such as O(n^2)) for arbitrary graphs, assuming P != NP. Therefore, we must abstain.

## Implementation Steps
1. Modify `get_optimal_tour` in `main.py` to raise a `ValueError` with the exact message 'P != NP'.
2. Write tests in `test_main.py` to verify that calling `get_optimal_tour` raises this specific `ValueError`.
3. Verify the tests by running them.
