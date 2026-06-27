# Plan for verify_topological_sort

1.  **Check Nodes Exactly Once**: Ensure the `order` contains the exact same number of nodes as the `graph` keys. We can check `len(order) == len(graph)`. Also, checking `len(set(order)) == len(order)` ensures there are no duplicates in `order`.
2.  **Node Set Match**: Ensure `set(order) == set(graph.keys())`.
3.  **Position Mapping**: Create a dictionary mapping each node to its index in `order` for O(1) lookups.
4.  **Edge Verification**: Iterate over each node `u` and its neighbors `v` in the `graph`:
    *   Verify `v` is in the `order` mapping. If not, return False.
    *   Verify that `u` appears before `v` by checking if `position_map[u] < position_map[v]`. If not, return False.
5.  If all checks pass, return True.
