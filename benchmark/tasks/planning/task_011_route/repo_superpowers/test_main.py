import pytest
from main import plan_delivery_route

def test_simple_route():
    grid = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
    start = (1, 1)
    waypoints = [(0, 0), (0, 2), (2, 0), (2, 2)]
    assert plan_delivery_route(grid, start, waypoints) == 8

def test_with_obstacles():
    grid = [
        [0, 1, 0],
        [0, 1, 0],
        [0, 0, 0]
    ]
    start = (0, 0)
    waypoints = [(0, 2)]
    assert plan_delivery_route(grid, start, waypoints) == 6

def test_multiple_waypoints_obstacles():
    grid = [
        [0, 1, 0, 1, 0],
        [0, 1, 0, 1, 0],
        [0, 0, 0, 0, 0]
    ]
    start = (0, 0)
    waypoints = [(0, 2), (0, 4)]
    assert plan_delivery_route(grid, start, waypoints) == 12

def test_unreachable():
    grid = [
        [0, 1, 0],
        [0, 1, 0],
        [0, 1, 0]
    ]
    start = (0, 0)
    waypoints = [(0, 2)]
    assert plan_delivery_route(grid, start, waypoints) == -1

def test_start_is_waypoint():
    grid = [
        [0, 0],
        [0, 0]
    ]
    start = (0, 0)
    waypoints = [(0, 0), (1, 1)]
    assert plan_delivery_route(grid, start, waypoints) == 2

def test_no_waypoints():
    grid = [[0, 0], [0, 0]]
    start = (0, 0)
    waypoints = []
    assert plan_delivery_route(grid, start, waypoints) == 0
