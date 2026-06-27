import heapq
import collections

def min_delivery_distance(battery_capacity: int, packages: list[dict], stations: list[tuple[int, int]]) -> int:
    K = len(packages)
    S = len(stations)
    
    nodes = [(0, 0)]
    for p in packages:
        nodes.append(p['pickup'])
    for p in packages:
        nodes.append(p['dropoff'])
    for st in stations:
        nodes.append(st)
        
    def get_dist(u, v):
        return abs(nodes[u][0] - nodes[v][0]) + abs(nodes[u][1] - nodes[v][1])
        
    # Priority Queue: (distance, u, uncompleted_mask, carried_pkg, battery)
    pq = [(0, 0, (1 << K) - 1, -1, battery_capacity)]
    
    # max_b[state] stores the max battery we had when arriving at this state
    # state: (u, mask, carried)
    max_b = collections.defaultdict(lambda: -1)
    
    while pq:
        d, u, mask, carried, b = heapq.heappop(pq)
        
        state_key = (u, mask, carried)
        if b <= max_b[state_key]:
            continue
        max_b[state_key] = b
        
        if mask == 0:
            return d
            
        # 1. Stations
        for i in range(S):
            v = 1 + 2*K + i
            cost = get_dist(u, v)
            if b >= cost:
                next_b = battery_capacity
                if next_b > max_b[(v, mask, carried)]:
                    heapq.heappush(pq, (d + cost, v, mask, carried, next_b))
                    
        # 2. Pickups
        if carried == -1:
            for i in range(K):
                if mask & (1 << i):
                    v = 1 + i
                    cost = get_dist(u, v)
                    if b >= cost:
                        next_b = b - cost
                        if next_b > max_b[(v, mask, i)]:
                            heapq.heappush(pq, (d + cost, v, mask, i, next_b))
                            
        # 3. Dropoff
        if carried != -1:
            v = 1 + K + carried
            cost = get_dist(u, v)
            if b >= cost:
                next_b = b - cost
                next_mask = mask ^ (1 << carried)
                if next_b > max_b[(v, next_mask, -1)]:
                    heapq.heappush(pq, (d + cost, v, next_mask, -1, next_b))

    return -1
