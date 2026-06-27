def verify_topological_sort(graph: dict, order: list) -> bool:
    if len(order) != len(graph) or set(order) != set(graph.keys()):
        return False
    
    positions = {node: i for i, node in enumerate(order)}
    
    for u, neighbors in graph.items():
        for v in neighbors:
            if v not in positions or positions[u] >= positions[v]:
                return False
                
    return True
