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

def test_empty_packages():
    assert min_delivery_distance(10, [], []) == 0

def test_no_battery_to_move():
    # Pickup at (2, 0) requires 2 battery, but B = 1.
    assert min_delivery_distance(1, [{"pickup": (2, 0), "dropoff": (3, 0)}], []) == -1

def test_start_is_station_and_pickup():
    # Start at (0,0), which is also a pickup and a station.
    # Package at (0,0) to (2,0).
    # Since we start at (0,0), we can pickup immediately and move to (2,0).
    # Dist = 2.
    assert min_delivery_distance(5, [{"pickup": (0, 0), "dropoff": (2, 0)}], [(0, 0)]) == 2

def test_identical_packages():
    # Two identical packages from (1, 1) to (2, 2).
    # Route: (0,0) -> (1,1) [pickup 1] -> (2,2) [dropoff 1] -> (1,1) [pickup 2] -> (2,2) [dropoff 2]
    # Dist: 2 + 2 + 2 + 2 = 8
    packages = [
        {"pickup": (1, 1), "dropoff": (2, 2)},
        {"pickup": (1, 1), "dropoff": (2, 2)}
    ]
    assert min_delivery_distance(10, packages, []) == 8

def test_optimal_ordering():
    # Going to package 2 first is shorter (total 8) than package 1 first (total 10).
    packages = [
        {"pickup": (2, 0), "dropoff": (4, 0)},
        {"pickup": (-1, 0), "dropoff": (-2, 0)}
    ]
    assert min_delivery_distance(10, packages, []) == 8

def test_multiple_recharges():
    # B = 4.
    # Start (0,0) -> station (3,0) [dist 3, recharge to 4]
    # -> station (6,0) [dist 3, recharge to 4]
    # -> pickup (8,0) [dist 2, bat 2, pickup]
    # -> dropoff (10,0) [dist 2, bat 0, dropoff]
    # Total dist = 3 + 3 + 2 + 2 = 10
    packages = [{"pickup": (8, 0), "dropoff": (10, 0)}]
    stations = [(3, 0), (6, 0)]
    assert min_delivery_distance(4, packages, stations) == 10

def test_recharge_before_pickup():
    # B = 4.
    # Start (0,0) -> station (2,1) [dist 3, recharge to 4]
    # -> pickup (3,0) [dist 2, bat 2, pickup]
    # -> dropoff (5,0) [dist 2, bat 0, dropoff]
    # Total dist = 3 + 2 + 2 = 7.
    # Going (0,0) -> (3,0) [pickup] directly is possible (dist 3, bat 1),
    # but then we can't reach the station at (2,1) (dist 2 > bat 1).
    packages = [{"pickup": (3, 0), "dropoff": (5, 0)}]
    stations = [(2, 1)]
    assert min_delivery_distance(4, packages, stations) == 7

def test_no_solution_due_to_battery():
    # B = 5.
    # Package: (3,0) to (6,0). Total dist to deliver is 6, which exceeds capacity.
    packages = [{"pickup": (3, 0), "dropoff": (6, 0)}]
    assert min_delivery_distance(5, packages, []) == -1


