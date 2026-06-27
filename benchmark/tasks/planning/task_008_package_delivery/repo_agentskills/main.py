from collections import deque

def bfs(grid: list[str], start: tuple[int, int], target: tuple[int, int]) -> list[str] | None:
    if start == target:
        return []
    
    rows, cols = len(grid), len(grid[0])
    queue = deque([start])
    parent = {start: (None, None)}  # maps cell -> (parent_cell, move_to_get_here)
    
    while queue:
        r, c = queue.popleft()
        
        if (r, c) == target:
            path = []
            curr = (r, c)
            while curr != start:
                prev, move = parent[curr]
                path.append(move)
                curr = prev
            return path[::-1]
            
        for dr, dc, move in [(-1, 0, "UP"), (1, 0, "DOWN"), (0, -1, "LEFT"), (0, 1, "RIGHT")]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] != 'X' and (nr, nc) not in parent:
                parent[(nr, nc)] = ((r, c), move)
                queue.append((nr, nc))
                
    return None

def plan_delivery_route(grid: list[str]) -> list[str] | None:
    if not grid or not grid[0]:
        return None
        
    start_pos = None
    packages = {}
    
    for r, row in enumerate(grid):
        for c, val in enumerate(row):
            if val == 'S':
                start_pos = (r, c)
            elif val.isalpha() and val != 'X':
                packages[val] = (r, c)
                
    if not start_pos:
        return None
        
    targets = sorted(packages.keys())
    current_pos = start_pos
    full_path = []
    
    for target_char in targets:
        target_pos = packages[target_char]
        path_segment = bfs(grid, current_pos, target_pos)
        if path_segment is None:
            return None
        full_path.extend(path_segment)
        current_pos = target_pos
        
    return full_path

