import itertools
from collections import deque
from typing import List, Tuple

def plan_delivery_route(grid: List[List[int]], start: Tuple[int, int], waypoints: List[Tuple[int, int]]) -> int:
    if not waypoints:
        return 0
        
    nodes = [start] + waypoints
    n = len(nodes)
    
    rows = len(grid)
    if rows == 0: return -1
    cols = len(grid[0])
    
    dist = [[float('inf')] * n for _ in range(n)]
    
    for i, (sr, sc) in enumerate(nodes):
        q = deque([(sr, sc)])
        visited = [[False] * cols for _ in range(rows)]
        visited[sr][sc] = True
        
        node_dist = [[float('inf')] * cols for _ in range(rows)]
        node_dist[sr][sc] = 0
        
        while q:
            r, c = q.popleft()
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 0 and not visited[nr][nc]:
                    visited[nr][nc] = True
                    node_dist[nr][nc] = node_dist[r][c] + 1
                    q.append((nr, nc))
                    
        for j, (er, ec) in enumerate(nodes):
            dist[i][j] = node_dist[er][ec]
            
    for j in range(1, n):
        if dist[0][j] == float('inf'):
            return -1
            
    min_steps = float('inf')
    waypoint_indices = list(range(1, n))
    for perm in itertools.permutations(waypoint_indices):
        curr_dist = 0
        curr_node = 0
        for next_node in perm:
            curr_dist += dist[curr_node][next_node]
            curr_node = next_node
        if curr_dist < min_steps:
            min_steps = curr_dist
            
    return int(min_steps) if min_steps != float('inf') else -1
