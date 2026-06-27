import heapq

def min_delivery_distance(battery_capacity: int, packages: list[dict], stations: list[tuple[int, int]]) -> int:
    # 1. Identify all unique POIs
    start_loc = (0, 0)
    pois_set = {start_loc}
    for s in stations:
        pois_set.add(tuple(s))
    for p in packages:
        pois_set.add(tuple(p["pickup"]))
        pois_set.add(tuple(p["dropoff"]))
        
    pois = [start_loc] + sorted(list(pois_set - {start_loc}))
    poi_to_idx = {poi: i for i, poi in enumerate(pois)}
    num_pois = len(pois)
    
    # 2. Precompute distance matrix
    dist_matrix = [[0] * num_pois for _ in range(num_pois)]
    for i in range(num_pois):
        x1, y1 = pois[i]
        for j in range(i + 1, num_pois):
            x2, y2 = pois[j]
            d = abs(x1 - x2) + abs(y1 - y2)
            dist_matrix[i][j] = d
            dist_matrix[j][i] = d
            
    # 3. Map stations and packages to POI indices
    stations_indices = {poi_to_idx[tuple(s)] for s in stations}
    n_packages = len(packages)
    pickups = [poi_to_idx[tuple(p["pickup"])] for p in packages]
    dropoffs = [poi_to_idx[tuple(p["dropoff"])] for p in packages]
    
    # Target delivered bitmask
    target_delivered = (1 << n_packages) - 1
    
    # Priority queue: (dist, loc_idx, deliv, carr, bat)
    pq = [(0, 0, 0, -1, battery_capacity)]
    best_bat = {}
    
    while pq:
        d, loc, deliv, carr, bat = heapq.heappop(pq)
        
        # 4. Automatic Actions (0-cost)
        # Drop off carried package if at its dropoff
        if carr != -1 and loc == dropoffs[carr]:
            deliv |= (1 << carr)
            carr = -1
            
        # Recharge if at a station
        if loc in stations_indices:
            bat = battery_capacity
            
        # Check goal
        if deliv == target_delivered:
            return d
            
        # Pruning check
        state_key = (loc, deliv, carr)
        if best_bat.get(state_key, -1) >= bat:
            continue
        best_bat[state_key] = bat
        
        # 5. Branching Actions
        if carr == -1:
            # Pick up any package at current location
            for i in range(n_packages):
                if pickups[i] == loc and not (deliv & (1 << i)):
                    heapq.heappush(pq, (d, loc, deliv, i, bat))
            
            # Move to any station or pickup of undelivered package
            nxt_targets = set()
            for s_idx in stations_indices:
                if s_idx != loc:
                    nxt_targets.add(s_idx)
            for i in range(n_packages):
                if not (deliv & (1 << i)):
                    p_idx = pickups[i]
                    if p_idx != loc:
                        nxt_targets.add(p_idx)
                        
            for nxt_loc in nxt_targets:
                dist_move = dist_matrix[loc][nxt_loc]
                if bat >= dist_move:
                    heapq.heappush(pq, (d + dist_move, nxt_loc, deliv, carr, bat - dist_move))
                    
        else:
            # Move to any station or the dropoff of the carried package
            nxt_targets = set()
            for s_idx in stations_indices:
                if s_idx != loc:
                    nxt_targets.add(s_idx)
            d_idx = dropoffs[carr]
            if d_idx != loc:
                nxt_targets.add(d_idx)
                
            for nxt_loc in nxt_targets:
                dist_move = dist_matrix[loc][nxt_loc]
                if bat >= dist_move:
                    heapq.heappush(pq, (d + dist_move, nxt_loc, deliv, carr, bat - dist_move))
                    
    return -1
