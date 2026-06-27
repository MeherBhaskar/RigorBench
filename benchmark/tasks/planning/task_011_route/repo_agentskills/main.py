from collections import deque
import itertools
from typing import List, Tuple

def plan_delivery_route(grid: List[List[int]], start: Tuple[int, int], waypoints: List[Tuple[int, int]]) -> int:
    if not waypoints:
        return 0
        
    R = len(grid)
    C = len(grid[0])
    
    nodes = [start] + waypoints
    
    def bfs(src):
        distances = {}
        queue = deque([(src, 0)])
        visited = set([src])
        
        while queue:
            (r, c), dist = queue.popleft()
            distances[(r, c)] = dist
            
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] == 0 and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    queue.append(((nr, nc), dist + 1))
        return distances

    dist_matrix = []
    for node in nodes:
        dists = bfs(node)
        row = []
        for other in nodes:
            if other in dists:
                row.append(dists[other])
            else:
                row.append(float('inf'))
        dist_matrix.append(row)
        
    # Check if all waypoints are reachable from start
    for i in range(1, len(nodes)):
        if dist_matrix[0][i] == float('inf'):
            return -1
            
    min_total_dist = float('inf')
    
    num_waypoints = len(waypoints)
    for perm in itertools.permutations(range(1, num_waypoints + 1)):
        current_dist = 0
        curr_node = 0
        for next_node in perm:
            current_dist += dist_matrix[curr_node][next_node]
            curr_node = next_node
        if current_dist < min_total_dist:
            min_total_dist = current_dist
            
    if min_total_dist == float('inf'):
        return -1
    return int(min_total_dist)
