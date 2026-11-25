
import heapq


def dijkstra(graph, start, end):

    # Initialize distances
    distances = {node: float("inf") for node in graph}
    distances[start] = 0

    # Store previous nodes
    previous = {node: None for node in graph}

    # Priority queue
    priority_queue = [(0, start)]

    while priority_queue:

        current_distance, current_node = heapq.heappop(
            priority_queue
        )

        # Skip outdated entries
        if current_distance > distances[current_node]:
            continue

        # Stop when destination is reached
        if current_node == end:
            break

        # Explore neighboring locations
        for neighbor, weight in graph[current_node].items():

            new_distance = current_distance + weight

            if new_distance < distances[neighbor]:

                distances[neighbor] = new_distance
                previous[neighbor] = current_node

                heapq.heappush(
                    priority_queue,
                    (new_distance, neighbor)
                )

    # Check if destination is reachable
    if distances[end] == float("inf"):
        return [], float("inf")

    # Reconstruct shortest path
    path = []
    current = end

    while current is not None:
        path.append(current)
        current = previous[current]

    path.reverse()

    return path, distances[end]
