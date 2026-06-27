def verify_topological_sort(graph: dict, order: list) -> bool:
    all_nodes = set(graph.keys())
    for neighbors in graph.values():
        all_nodes.update(neighbors)
        
    if len(order) != len(all_nodes) or set(order) != all_nodes:
        return False
        
    order_index = {node: i for i, node in enumerate(order)}
    
    for u, neighbors in graph.items():
        for v in neighbors:
            if order_index[u] >= order_index[v]:
                return False
                
    return True
