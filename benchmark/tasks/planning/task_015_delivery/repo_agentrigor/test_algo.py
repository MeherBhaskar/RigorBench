from main import min_delivery_distance

print("Test 1:", min_delivery_distance(10, [{"pickup": (2, 2), "dropoff": (4, 4)}], []))
print("Test 2:", min_delivery_distance(5, [{"pickup": (2, 2), "dropoff": (4, 4)}], [(2, 2)]))

packages = [
    {"pickup": (0, 1), "dropoff": (0, 2)},
    {"pickup": (0, 3), "dropoff": (0, 4)}
]
print("Test 3:", min_delivery_distance(10, packages, []))

packages = [{"pickup": (3, 0), "dropoff": (6, 0)}]
stations = [(3, 2)]
print("Test 4:", min_delivery_distance(4, packages, stations))

packages = [{"pickup": (3, 0), "dropoff": (6, 0)}]
stations = [(3, 1)]
print("Test 5:", min_delivery_distance(4, packages, stations))
