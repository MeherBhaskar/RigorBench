import sys
from solution import plan_delivery_route

def test():
    grid = [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]
    ]
    start = (1, 0)
    waypoints = [(1, 2), (0, 0)]
    
    res = plan_delivery_route(grid, start, waypoints)
    print(f"Result: {res}")
    assert res == 4

if __name__ == "__main__":
    test()
