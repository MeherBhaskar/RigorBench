from main import plan_delivery_route

def verify_path(grid, path):
    if path is None:
        return False
    r, c = -1, -1
    packages = {}
    for i, row in enumerate(grid):
        for j, val in enumerate(row):
            if val == 'S':
                r, c = i, j
            elif val.isalpha() and val not in ('S', 'X'):
                packages[val] = (i, j)
    
    if r == -1:
        return False
    
    collected = []
    target_char = 'A'
    
    for move in path:
        if move == "UP": r -= 1
        elif move == "DOWN": r += 1
        elif move == "LEFT": c -= 1
        elif move == "RIGHT": c += 1
        else: return False
        
        if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or grid[r][c] == 'X':
            return False
            
        for p, pos in packages.items():
            if pos == (r, c) and p == target_char:
                collected.append(p)
                target_char = chr(ord(target_char) + 1)
                break
                    
    return len(collected) == len(packages)

def test_simple_route():
    grid = [
        "S..",
        "XX.",
        "B.A"
    ]
    path = plan_delivery_route(grid)
    assert verify_path(grid, path)
    assert len(path) == 6

def test_unreachable():
    grid = [
        "S.X",
        "XXX",
        "..A"
    ]
    assert plan_delivery_route(grid) is None

def test_complex_route():
    grid = [
        "S.X.A",
        ".XXX.",
        "...X.",
        "XX.X.",
        "C...B"
    ]
    path = plan_delivery_route(grid)
    assert verify_path(grid, path)
    assert len(path) == 20
def test_no_packages():
    grid = [
        "S..",
        "...",
        "..."
    ]
    path = plan_delivery_route(grid)
    assert path == []

def test_single_package():
    grid = [
        "S..",
        ".X.",
        "..A"
    ]
    path = plan_delivery_route(grid)
    assert verify_path(grid, path)
    assert len(path) == 4

def test_no_start_pos():
    grid = [
        "...",
        ".X.",
        "..A"
    ]
    assert plan_delivery_route(grid) is None

def test_passing_through_future_package():
    grid = [
        "S.B.A"
    ]
    path = plan_delivery_route(grid)
    assert verify_path(grid, path)
    assert path == ["RIGHT", "RIGHT", "RIGHT", "RIGHT", "LEFT", "LEFT"]

def test_empty_grid():
    assert plan_delivery_route([]) is None
    assert plan_delivery_route([""]) is None

def test_large_grid():
    grid = []
    for r in range(50):
        if r == 0:
            grid.append("S" + "." * 49)
        elif r == 49:
            grid.append("." * 49 + "A")
        else:
            grid.append("." * 50)
    path = plan_delivery_route(grid)
    assert verify_path(grid, path)
    assert len(path) == 98

def test_complex_winding_path():
    grid = [
        "SXX.B",
        ".XX.X",
        ".XX.X",
        "....X",
        "AXXXX"
    ]
    path = plan_delivery_route(grid)
    assert verify_path(grid, path)
    assert len(path) == 12
