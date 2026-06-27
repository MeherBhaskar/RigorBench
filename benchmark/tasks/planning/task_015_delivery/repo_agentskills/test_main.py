from main import min_delivery_distance

def test_simple_delivery():
    assert min_delivery_distance(10, [{"pickup": (2, 2), "dropoff": (4, 4)}], []) == 8

def test_requires_recharge():
    assert min_delivery_distance(5, [{"pickup": (2, 2), "dropoff": (4, 4)}], [(2, 2)]) == 8

def test_impossible_reach():
    assert min_delivery_distance(3, [{"pickup": (2, 2), "dropoff": (4, 4)}], [(2, 2)]) == -1

def test_multiple_packages():
    packages = [
        {"pickup": (0, 1), "dropoff": (0, 2)},
        {"pickup": (0, 3), "dropoff": (0, 4)}
    ]
    assert min_delivery_distance(10, packages, []) == 4

def test_recharge_detour():
    packages = [{"pickup": (3, 0), "dropoff": (6, 0)}]
    stations = [(3, 2)]
    assert min_delivery_distance(4, packages, stations) == -1

def test_recharge_detour_possible():
    packages = [{"pickup": (3, 0), "dropoff": (6, 0)}]
    stations = [(3, 1)]
    assert min_delivery_distance(4, packages, stations) == 8

def test_empty_packages():
    # If there are no packages to deliver, the distance should be 0.
    assert min_delivery_distance(10, [], []) == 0

def test_package_pickup_and_dropoff_same():
    # If pickup and dropoff are at the same location, distance is just to get to that location and back/onward.
    # 0,0 -> 2,2 (dist 4, pickup & dropoff at 2,2) -> total 4.
    packages = [{"pickup": (2, 2), "dropoff": (2, 2)}]
    assert min_delivery_distance(10, packages, []) == 4

def test_multiple_packages_with_shared_locations():
    # Two packages, sharing pickup or dropoff.
    # Package 1: (0, 1) -> (0, 2)
    # Package 2: (0, 1) -> (0, 3)
    # Start: (0, 0).
    # Optimal:
    # 0,0 -> 0,1 (dist 1, pick 1) -> 0,2 (dist 1, drop 1) -> 0,1 (dist 1, pick 2) -> 0,3 (dist 2, drop 2) -> total 5.
    packages = [
        {"pickup": (0, 1), "dropoff": (0, 2)},
        {"pickup": (0, 1), "dropoff": (0, 3)}
    ]
    assert min_delivery_distance(10, packages, []) == 5

def test_zero_capacity_unreachable():
    # If battery capacity is too small to make even the first move, it's impossible.
    packages = [{"pickup": (2, 2), "dropoff": (4, 4)}]
    assert min_delivery_distance(1, packages, []) == -1

def test_start_is_station():
    # Start at (0, 0), which is also a station.
    packages = [{"pickup": (2, 2), "dropoff": (4, 4)}]
    stations = [(0, 0)]
    assert min_delivery_distance(10, packages, stations) == 8

def test_duplicate_packages():
    # Multiple identical packages.
    # Package 1: (1, 0) -> (2, 0)
    # Package 2: (1, 0) -> (2, 0)
    # Optimal route:
    # 0,0 -> 1,0 (dist 1, pick 1) -> 2,0 (dist 1, drop 1) -> 1,0 (dist 1, pick 2) -> 2,0 (dist 1, drop 2) -> total 4.
    packages = [
        {"pickup": (1, 0), "dropoff": (2, 0)},
        {"pickup": (1, 0), "dropoff": (2, 0)}
    ]
    assert min_delivery_distance(10, packages, []) == 4

def test_impossible_to_deliver_all():
    # One package can be delivered, but the other cannot. Should return -1.
    packages = [
        {"pickup": (1, 0), "dropoff": (2, 0)},      # Easy
        {"pickup": (100, 0), "dropoff": (101, 0)}   # Impossible with B=10
    ]
    assert min_delivery_distance(10, packages, []) == -1
