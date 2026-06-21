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
