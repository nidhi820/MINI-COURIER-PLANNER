
import json

from algorithms.tsp import nearest_neighbor_tsp
from algorithms.dijkstra import dijkstra
from algorithms.sorting import prioritize_parcels
from algorithms.knapsack import knapsack

# Load parcel data
with open("data/parcels.json", "r") as file:
    parcels = json.load(file)

# STEP 1: Sort parcels
sorted_parcels = prioritize_parcels(parcels)

print("\n===== PARCEL PRIORITIZATION =====")

for parcel in sorted_parcels:
    print(
        f"ID: {parcel['id']} | "
        f"Priority: {parcel['priority']} | "
        f"Deadline: {parcel['deadline']} days"
    )

# STEP 2: Apply Knapsack Algorithm
capacity = 10

selected, total_weight, total_value, dp = knapsack(
    sorted_parcels, capacity
)

print("\n===== OPTIMAL PACKING PLAN =====")

for parcel in selected:
    print(
        f"Parcel: {parcel['id']} | "
        f"Weight: {parcel['weight']} kg | "
        f"Value: {parcel['value']}"
    )

print("\nTotal Weight:", total_weight, "kg")
print("Bag Capacity:", capacity, "kg")
print("Maximum Total Value:", total_value)


# STEP 3: Apply Dijkstra's Algorithm

with open("data/locations.json", "r") as file:
    graph = json.load(file)

start = "A"
end = "E"

path, distance = dijkstra(graph, start, end)

print("\n===== DIJKSTRA SHORTEST PATH =====")

if path:
    print("Starting Location:", start)
    print("Destination:", end)
    print("Shortest Route:", " -> ".join(path))
    print("Shortest Distance:", distance, "KM")
else:
    print("No route available.")


# STEP 4: Apply Nearest Neighbor TSP

route, total_distance = nearest_neighbor_tsp(
    graph, "A"
)

print("\n===== NEAREST NEIGHBOR TSP ROUTE =====")

if total_distance != float("inf"):
    print("Starting Location: A")
    print("Delivery Route:", " -> ".join(route))
    print("Total Route Distance:", total_distance, "KM")
else:
    print("A complete delivery tour is not possible.")
