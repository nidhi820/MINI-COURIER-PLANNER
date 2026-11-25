
from algorithms.dijkstra import dijkstra


def nearest_neighbor_tsp(graph, start):

    unvisited = set(graph.keys())
    unvisited.remove(start)

    current = start
    route = [start]
    total_distance = 0

    # Visit every unvisited location
    while unvisited:

        nearest_location = None
        shortest_distance = float("inf")
        shortest_path = []

        # Find the nearest unvisited location
        for location in unvisited:

            path, distance = dijkstra(
                graph, current, location
            )

            if distance < shortest_distance:
                shortest_distance = distance
                nearest_location = location
                shortest_path = path

        # No reachable location
        if nearest_location is None:
            return route, float("inf")

        # Add the shortest path to the route
        route.extend(shortest_path[1:])
        total_distance += shortest_distance

        current = nearest_location
        unvisited.remove(nearest_location)

    # Return to the starting location
    return_path, return_distance = dijkstra(
        graph, current, start
    )

    if not return_path:
        return route, float("inf")

    route.extend(return_path[1:])
    total_distance += return_distance

    return route, total_distance
