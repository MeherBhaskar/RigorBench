def verify_topological_sort(graph: dict, order: list) -> bool:
    if len(order) != len(graph) or len(set(order)) != len(order):
        return False
    
    if set(order) != set(graph.keys()):
        return False
        
    position_map = {node: i for i, node in enumerate(order)}
    
    for u, neighbors in graph.items():
        for v in neighbors:
            if v not in position_map:
                return False
            if position_map[u] > position_map[v]:
                return False
                
    return True
