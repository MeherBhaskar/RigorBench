from typing import List, Tuple
from collections import deque
import itertools

def plan_delivery_route(grid: List[List[int]], start: Tuple[int, int], waypoints: List[Tuple[int, int]]) -> int:
    if not waypoints:
        return 0

    rows = len(grid)
    if rows == 0: return -1
    cols = len(grid[0])
    
    unique_waypoints = list(set(waypoints))
    nodes = [start] + unique_waypoints
    
    def bfs(start_node):
        distances = {start_node: 0}
        queue = deque([start_node])
        while queue:
            r, c = queue.popleft()
            d = distances[(r, c)]
            
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 0:
                    if (nr, nc) not in distances:
                        distances[(nr, nc)] = d + 1
                        queue.append((nr, nc))
        return distances

    dist_matrix = {}
    for node in nodes:
        dist_matrix[node] = bfs(node)
        
    min_total_dist = float('inf')
    
    for perm in itertools.permutations(unique_waypoints):
        current_dist = 0
        current_node = start
        possible = True
        
        for next_node in perm:
            if next_node not in dist_matrix[current_node]:
                possible = False
                break
            current_dist += dist_matrix[current_node][next_node]
            current_node = next_node
            
        if possible:
            min_total_dist = min(min_total_dist, current_dist)
            
    if min_total_dist == float('inf'):
        return -1
        
    return min_total_dist
