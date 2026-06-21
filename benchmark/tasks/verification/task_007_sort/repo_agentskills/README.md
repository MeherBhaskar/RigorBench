# Prompt
Write a function `verify_topological_sort(graph: dict, order: list) -> bool` that verifies if the given `order` is a valid topological sort for the directed graph `graph`.

The `graph` is represented as an adjacency list where keys are node integers and values are lists of node integers they point to. The `order` is a list of node integers.

Return True if the order is valid, False otherwise. A valid topological sort must contain all nodes in the graph exactly once, and for every directed edge U -> V, U must appear before V in the order.