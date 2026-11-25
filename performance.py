
import time
import random
import csv
import os
import matplotlib.pyplot as plt

from algorithms.sorting import prioritize_parcels
from algorithms.knapsack import knapsack
from algorithms.dijkstra import dijkstra
from algorithms.tsp import nearest_neighbor_tsp


# Create results folder
os.makedirs("results", exist_ok=True)

# Measure average execution time
def measure_time(function, repetitions=3):

    total = 0

    for _ in range(repetitions):
        start = time.perf_counter()
        function()
        end = time.perf_counter()

        total += end - start

    return total / repetitions


# Generate sample parcels
def generate_parcels(n):

    rng = random.Random(42)

    parcels = []

    for i in range(n):

        parcels.append({
            "id": f"P{i}",
            "weight": rng.randint(1, 10),
            "value": rng.randint(100, 1000),
            "priority": rng.randint(1, 3),
            "deadline": rng.randint(1, 10)
        })

    return parcels


# Generate a connected weighted graph
def generate_graph(n):

    rng = random.Random(42)

    graph = {
        str(i): {} for i in range(n)
    }

    for i in range(n):
        for j in range(i + 1, n):

            distance = rng.randint(1, 30)

            graph[str(i)][str(j)] = distance
            graph[str(j)][str(i)] = distance

    return graph


# Store performance results
results = []


# 1. Sorting and Knapsack Testing
parcel_sizes = [10, 50, 100, 500, 1000]

sorting_times = []
knapsack_times = []

print("\n===== PARCEL ALGORITHM PERFORMANCE =====")

for size in parcel_sizes:

    parcels = generate_parcels(size)

    sorting_time = measure_time(
        lambda: prioritize_parcels(parcels)
    )

    knapsack_time = measure_time(
        lambda: knapsack(parcels, 100)
    )

    sorting_times.append(sorting_time)
    knapsack_times.append(knapsack_time)

    results.append([
        "Merge Sort", size, sorting_time
    ])

    results.append([
        "Knapsack", size, knapsack_time
    ])

    print(
        f"Parcels: {size} | "
        f"Sorting: {sorting_time:.6f}s | "
        f"Knapsack: {knapsack_time:.6f}s"
    )


# 2. Dijkstra Testing
graph_sizes = [10, 20, 40, 80]

dijkstra_times = []

print("\n===== DIJKSTRA PERFORMANCE =====")

for size in graph_sizes:

    graph = generate_graph(size)

    dijkstra_time = measure_time(
        lambda: dijkstra(graph, "0", str(size - 1))
    )

    dijkstra_times.append(dijkstra_time)

    results.append([
        "Dijkstra", size, dijkstra_time
    ])

    print(
        f"Locations: {size} | "
        f"Time: {dijkstra_time:.6f}s"
    )


# 3. TSP Testing
tsp_sizes = [5, 8, 10, 12]

tsp_times = []

print("\n===== TSP PERFORMANCE =====")

for size in tsp_sizes:

    graph = generate_graph(size)

    tsp_time = measure_time(
        lambda: nearest_neighbor_tsp(graph, "0"),
        repetitions=2
    )

    tsp_times.append(tsp_time)

    results.append([
        "Nearest Neighbor TSP", size, tsp_time
    ])

    print(
        f"Locations: {size} | "
        f"Time: {tsp_time:.6f}s"
    )


# Save results in CSV
with open(
    "results/performance_results.csv",
    "w",
    newline=""
) as file:

    writer = csv.writer(file)

    writer.writerow([
        "Algorithm",
        "Input Size",
        "Execution Time (seconds)"
    ])

    writer.writerows(results)


# Create runtime charts
def create_chart(sizes, times, title, filename):

    plt.figure(figsize=(8, 5))

    plt.plot(
        sizes,
        times,
        marker="o",
        label="Execution Time"
    )

    plt.xlabel("Input Size")
    plt.ylabel("Execution Time (seconds)")
    plt.title(title)

    plt.grid(True)
    plt.legend()

    plt.savefig(f"results/{filename}")
    plt.close()


create_chart(
    parcel_sizes,
    sorting_times,
    "Merge Sort Performance",
    "merge_sort.png"
)

create_chart(
    parcel_sizes,
    knapsack_times,
    "Knapsack Performance",
    "knapsack.png"
)

create_chart(
    graph_sizes,
    dijkstra_times,
    "Dijkstra Performance",
    "dijkstra.png"
)

create_chart(
    tsp_sizes,
    tsp_times,
    "Nearest Neighbor TSP Performance",
    "tsp.png"
)


print("\n===== PERFORMANCE TESTING COMPLETED =====")
print("CSV file saved in results folder.")
print("Runtime charts saved in results folder.")
