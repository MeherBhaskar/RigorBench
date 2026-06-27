from collections import deque

def plan_delivery_route(grid, start, waypoints):
    if not waypoints:
        return 0
        
    R = len(grid)
    if R == 0:
        return -1
    C = len(grid[0])
    
    unique_waypoints = []
    for wp in waypoints:
        if wp not in unique_waypoints and wp != start:
            unique_waypoints.append(wp)
            
    if not unique_waypoints:
        return 0

    nodes = [start] + unique_waypoints
    n = len(nodes)
    node_to_idx = {node: i for i, node in enumerate(nodes)}
    
    dist = [[float('inf')] * n for _ in range(n)]
    
    for i in range(n):
        sr, sc = nodes[i]
        # Start node could be on an obstacle, but we assume we are already there.
        # But we can only move to adjacent 0s.
        queue = deque([(sr, sc, 0)])
        visited = set([(sr, sc)])
        
        while queue:
            r, c, d = queue.popleft()
            
            if (r, c) in node_to_idx:
                dist[i][node_to_idx[(r, c)]] = d
                
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < R and 0 <= nc < C and (nr, nc) not in visited:
                    if grid[nr][nc] == 0:
                        visited.add((nr, nc))
                        queue.append((nr, nc, d + 1))
                        
    for j in range(1, n):
        if dist[0][j] == float('inf'):
            return -1
            
    memo = {}
    def dfs(curr, mask):
        if mask == (1 << n) - 1:
            return 0
        if (curr, mask) in memo:
            return memo[(curr, mask)]
            
        min_cost = float('inf')
        for nxt in range(1, n):
            if not (mask & (1 << nxt)):
                min_cost = min(min_cost, dist[curr][nxt] + dfs(nxt, mask | (1 << nxt)))
                
        memo[(curr, mask)] = min_cost
        return min_cost
        
    ans = dfs(0, 1)
    return ans if ans != float('inf') else -1
