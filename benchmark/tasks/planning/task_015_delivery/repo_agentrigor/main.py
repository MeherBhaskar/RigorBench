import heapq

def min_delivery_distance(battery_capacity: int, packages: list[dict], stations: list[tuple[int, int]]) -> int:
    # 1. Identify and index all points of interest (POIs)
    coords = set([(0, 0)])
    for p in packages:
        coords.add(p["pickup"])
        coords.add(p["dropoff"])
    for s in stations:
        coords.add(s)
    
    coord_list = list(coords)
    n_coords = len(coord_list)
    
    stations_set = set(stations)
    is_station = [c in stations_set for c in coord_list]
    
    # Map package pickup/dropoff to coord indices
    package_pickup_indices = [coord_list.index(p["pickup"]) for p in packages]
    package_dropoff_indices = [coord_list.index(p["dropoff"]) for p in packages]
    station_indices = [coord_list.index(s) for s in stations]
    
    # Store pickup/dropoff packages at each coordinate for free actions
    pickups = [[] for _ in range(n_coords)]
    dropoffs = [[] for _ in range(n_coords)]
    for i, p in enumerate(packages):
        p_idx = package_pickup_indices[i]
        d_idx = package_dropoff_indices[i]
        pickups[p_idx].append(i)
        dropoffs[d_idx].append(i)
        
    start_idx = coord_list.index((0, 0))
    
    # Priority Queue: (dist, -bat, u, delivered, carried)
    pq = [(0, -battery_capacity, start_idx, 0, -1)]
    max_battery_seen = {}
    target_delivered = (1 << len(packages)) - 1
    
    while pq:
        dist, neg_bat, u, delivered, carried = heapq.heappop(pq)
        bat = -neg_bat
        
        state_key = (u, delivered, carried)
        if bat <= max_battery_seen.get(state_key, -1):
            continue
        max_battery_seen[state_key] = bat
        
        if delivered == target_delivered:
            return dist
            
        # --- 1. Free Actions (Cost 0, Distance 0) ---
        if carried == -1:
            for p_idx in pickups[u]:
                if not (delivered & (1 << p_idx)):
                    next_state_key = (u, delivered, p_idx)
                    if bat > max_battery_seen.get(next_state_key, -1):
                        heapq.heappush(pq, (dist, -bat, u, delivered, p_idx))
                        
        if carried != -1:
            if carried in dropoffs[u]:
                next_delivered = delivered | (1 << carried)
                next_state_key = (u, next_delivered, -1)
                if bat > max_battery_seen.get(next_state_key, -1):
                    heapq.heappush(pq, (dist, -bat, u, next_delivered, -1))
                    
        # --- 2. Movement Transitions to Candidates ---
        # Candidates include:
        # - All charging stations
        # - If carried == -1: pickup of any undelivered package
        # - If carried != -1: dropoff of the carried package
        candidates = set(station_indices)
        if carried == -1:
            for i in range(len(packages)):
                if not (delivered & (1 << i)):
                    candidates.add(package_pickup_indices[i])
        else:
            candidates.add(package_dropoff_indices[carried])
            
        ux, uy = coord_list[u]
        for v in candidates:
            if u == v:
                continue
            vx, vy = coord_list[v]
            cost = abs(ux - vx) + abs(uy - vy)
            if bat >= cost:
                next_bat = bat - cost
                if is_station[v]:
                    next_bat = battery_capacity
                
                next_state_key = (v, delivered, carried)
                if next_bat > max_battery_seen.get(next_state_key, -1):
                    heapq.heappush(pq, (dist + cost, -next_bat, v, delivered, carried))
                    
    return -1

