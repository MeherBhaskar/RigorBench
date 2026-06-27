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
    # 0,0 -> 3,0 (dist 3, bat 1). Pick up.
    # Can't go 3,0 -> 6,0 direct (dist 3 > bat 1).
    # Must detour to 3,2 (dist 2, wait, bat 1 is not enough to reach 3,2 from 3,0!).
    # Oh, need to go to station first! 0,0 -> 3,2 (dist 5 -> impossible with bat 4)
    assert min_delivery_distance(4, packages, stations) == -1

def test_recharge_detour_possible():
    packages = [{"pickup": (3, 0), "dropoff": (6, 0)}]
    stations = [(3, 1)]
    # 0,0 -> 3,0 (dist 3, bat 1). Pickup. 
    # 3,0 -> 3,1 (dist 1, bat 0). Recharge! bat=4.
    # 3,1 -> 6,0 (dist 4, bat 0). Dropoff!
    # Dist = 3 + 1 + 4 = 8
    assert min_delivery_distance(4, packages, stations) == 8

def test_zero_packages():
    assert min_delivery_distance(10, [], []) == 0

def test_same_pickup_dropoff():
    packages = [{"pickup": (2, 2), "dropoff": (2, 2)}]
    assert min_delivery_distance(10, packages, []) == 4

def test_start_is_station():
    packages = [{"pickup": (2, 2), "dropoff": (4, 4)}]
    # Start is a station. Does not change the distance.
    assert min_delivery_distance(10, packages, [(0, 0)]) == 8

def test_multiple_recharges_same_station():
    # Package 1: (0, 0) -> (4, 0).
    # Station at (2, 0).
    # Battery capacity 2.
    # 0,0 -> 2,0 (dist 2). Recharge.
    # 2,0 -> 4,0 (dist 2). Dropoff.
    # Total dist = 4.
    packages = [{"pickup": (0, 0), "dropoff": (4, 0)}]
    stations = [(2, 0)]
    assert min_delivery_distance(2, packages, stations) == 4

def test_complex_multi_package_routing():
    # Two packages:
    # P1: pickup (1, 1), dropoff (2, 2)
    # P2: pickup (2, 2), dropoff (3, 3)
    # Stations: [(1, 1)]
    # B = 4
    # 0,0 -> 1,1 (dist 2). Pick up P1. Recharge.
    # 1,1 -> 2,2 (dist 2). Drop off P1. Pick up P2.
    # 2,2 -> 3,3 (dist 2). Drop off P2.
    # Total distance: 2 + 2 + 2 = 6.
    packages = [
        {"pickup": (1, 1), "dropoff": (2, 2)},
        {"pickup": (2, 2), "dropoff": (3, 3)}
    ]
    stations = [(1, 1)]
    assert min_delivery_distance(4, packages, stations) == 6

def test_deadlock_without_recharge():
    # If battery capacity is 2 and we need to go 3 units, it's impossible.
    packages = [{"pickup": (0, 0), "dropoff": (3, 0)}]
    assert min_delivery_distance(2, packages, []) == -1

