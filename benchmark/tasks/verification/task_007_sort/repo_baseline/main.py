def verify_topological_sort(graph: dict, order: list) -> bool:
    all_nodes = set(graph.keys())
    for neighbors in graph.values():
        all_nodes.update(neighbors)
        
    if all_nodes != set(order) or len(order) != len(set(order)):
        return False
        
    positions = {node: i for i, node in enumerate(order)}
    
    for u, neighbors in graph.items():
        for v in neighbors:
            if positions[u] >= positions[v]:
                return False
                
    return True
