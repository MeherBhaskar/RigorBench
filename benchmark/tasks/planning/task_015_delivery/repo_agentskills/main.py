import heapq

def min_delivery_distance(battery_capacity: int, packages: list[dict], stations: list[tuple[int, int]]) -> int:
    """
    Plan the optimal route for a delivery drone in a 2D grid to deliver a set of packages.
    Returns the minimum total distance the drone must travel to complete the mission,
    or -1 if it is impossible to deliver all packages.
    """
    B = battery_capacity
    P = len(packages)
    
    poi_coords = [(0, 0)]
    station_set = set(stations)
    
    for p in packages:
        if p['pickup'] not in poi_coords:
            poi_coords.append(p['pickup'])
        if p['dropoff'] not in poi_coords:
            poi_coords.append(p['dropoff'])
            
    for s in stations:
        if s not in poi_coords:
            poi_coords.append(s)
            
    num_pois = len(poi_coords)
    is_station = [ (c in station_set) for c in poi_coords ]
    station_indices = [ i for i in range(num_pois) if is_station[i] ]
    
    pkg_pickup = []
    pkg_dropoff = []
    for p in packages:
        pkg_pickup.append(poi_coords.index(p['pickup']))
        pkg_dropoff.append(poi_coords.index(p['dropoff']))
        
    def get_dist(u, v):
        return abs(poi_coords[u][0] - poi_coords[v][0]) + abs(poi_coords[u][1] - poi_coords[v][1])
        
    max_b_seen = {}
    pq = []
    
    # State in PQ: (cost, -battery, poi_index, carried_package_index, delivered_mask)
    # The drone starts at (0, 0) (poi_index = 0) with a fully charged battery B,
    # carrying no package (-1), and with no packages delivered (0).
    heapq.heappush(pq, (0, -B, 0, -1, 0))
    target_delivered = (1 << P) - 1
    
    while pq:
        cost, neg_b, u, carried, delivered = heapq.heappop(pq)
        b = -neg_b
        
        if delivered == target_delivered:
            return cost
            
        state_key = (u, carried, delivered)
        if state_key in max_b_seen and max_b_seen[state_key] >= b:
            continue
        max_b_seen[state_key] = b
        
        # 1. Move to a charging station (Stepping stone)
        for v in station_indices:
            if v != u:
                d = get_dist(u, v)
                if d <= b:
                    heapq.heappush(pq, (cost + d, -B, v, carried, delivered))
                    
        # 2. Pick up a package (if not currently carrying one)
        if carried == -1:
            for i in range(P):
                if not (delivered & (1 << i)):
                    v = pkg_pickup[i]
                    d = get_dist(u, v)
                    if d <= b:
                        new_b = B if is_station[v] else b - d
                        heapq.heappush(pq, (cost + d, -new_b, v, i, delivered))
                        
        # 3. Drop off the carried package
        else:
            v = pkg_dropoff[carried]
            d = get_dist(u, v)
            if d <= b:
                new_b = B if is_station[v] else b - d
                heapq.heappush(pq, (cost + d, -new_b, v, -1, delivered | (1 << carried)))
                
    return -1
