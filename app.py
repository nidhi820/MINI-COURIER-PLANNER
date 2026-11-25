
import json

from algorithms.sorting import prioritize_parcels
from algorithms.knapsack import knapsack
from algorithms.dijkstra import dijkstra
from algorithms.tsp import nearest_neighbor_tsp


# Load project data
def load_data():

    with open("data/parcels.json", "r") as file:
        parcels = json.load(file)

    with open("data/locations.json", "r") as file:
        graph = json.load(file)

    return parcels, graph


# Display all parcels
def show_parcels(parcels):

    print("\n===== PARCEL PRIORITIZATION =====")

    sorted_parcels = prioritize_parcels(parcels)

    for parcel in sorted_parcels:
        print(
            f"ID: {parcel['id']} | "
            f"Priority: {parcel['priority']} | "
            f"Deadline: {parcel['deadline']} days"
        )


# Optimize parcel packing
def pack_parcels(parcels):

    try:
        capacity = int(input("\nEnter bag capacity (kg): "))

        if capacity <= 0:
            print("Capacity must be greater than zero.")
            return

        selected, weight, value, dp = knapsack(
            parcels, capacity
        )

        print("\n===== OPTIMAL PACKING PLAN =====")

        for parcel in selected:
            print(
                f"{parcel['id']} | "
                f"Weight: {parcel['weight']} kg | "
                f"Value: {parcel['value']}"
            )

        print("\nTotal Weight:", weight, "kg")
        print("Maximum Total Value:", value)

    except ValueError:
        print("Please enter a valid number.")


# Find shortest route
def find_shortest_route(graph):

    locations = list(graph.keys())

    print("\nAvailable Locations:", ", ".join(locations))

    start = input("Enter starting location: ").strip()
    end = input("Enter destination: ").strip()

    if start not in graph or end not in graph:
        print("Invalid location.")
        return

    path, distance = dijkstra(graph, start, end)

    print("\n===== SHORTEST DELIVERY ROUTE =====")

    if path:
        print("Route:", " -> ".join(path))
        print("Distance:", distance, "KM")
    else:
        print("No route available.")


# Find complete delivery tour
def find_delivery_tour(graph):

    locations = list(graph.keys())

    print("\nAvailable Locations:", ", ".join(locations))

    start = input("Enter starting location: ").strip()

    if start not in graph:
        print("Invalid starting location.")
        return

    route, distance = nearest_neighbor_tsp(graph, start)

    print("\n===== DELIVERY TOUR =====")

    if distance != float("inf"):
        print("Route:", " -> ".join(route))
        print("Total Distance:", distance, "KM")
    else:
        print("A complete delivery tour is not possible.")


# Main application
def main():

    try:
        parcels, graph = load_data()

        while True:

            print("\n" + "=" * 45)
            print("       MINI COURIER PLANNER")
            print("=" * 45)

            print("1. View Prioritized Parcels")
            print("2. Optimize Parcel Packing")
            print("3. Find Shortest Delivery Route")
            print("4. Generate Complete Delivery Tour")
            print("5. Exit")

            choice = input("\nEnter your choice (1-5): ").strip()

            if choice == "1":
                show_parcels(parcels)

            elif choice == "2":
                pack_parcels(parcels)

            elif choice == "3":
                find_shortest_route(graph)

            elif choice == "4":
                find_delivery_tour(graph)

            elif choice == "5":
                print("\nThank you for using Mini Courier Planner!")
                break

            else:
                print("\nInvalid choice. Please select 1 to 5.")

    except FileNotFoundError:
        print("Error: Project data files were not found.")

    except (ValueError, KeyError, TypeError) as error:
        print("Error in project data:", error)


if __name__ == "__main__":
    main()
