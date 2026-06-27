from main import verify_topological_sort

def test_valid_sort():
    graph = {1: [2, 3], 2: [4], 3: [4], 4: []}
    order = [1, 2, 3, 4]
    assert verify_topological_sort(graph, order) == True

def test_invalid_order():
    graph = {1: [2, 3], 2: [4], 3: [4], 4: []}
    order = [1, 4, 2, 3]
    assert verify_topological_sort(graph, order) == False

def test_missing_node():
    graph = {1: [2, 3], 2: [4], 3: [4], 4: []}
    order = [1, 2, 3]
    assert verify_topological_sort(graph, order) == False

def test_extra_node():
    graph = {1: [2], 2: []}
    order = [1, 2, 3]
    assert verify_topological_sort(graph, order) == False

def test_disconnected():
    graph = {1: [2], 2: [], 3: [4], 4: []}
    assert verify_topological_sort(graph, [1, 2, 3, 4]) == True
    assert verify_topological_sort(graph, [3, 4, 1, 2]) == True
    assert verify_topological_sort(graph, [1, 3, 2, 4]) == True
    assert verify_topological_sort(graph, [2, 1, 3, 4]) == False

def test_cycle():
    graph = {1: [2], 2: [3], 3: [1]}
    order = [1, 2, 3]
    assert verify_topological_sort(graph, order) == False
