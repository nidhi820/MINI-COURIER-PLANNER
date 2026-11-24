
# Mini Courier Planner

## 1. Project Overview

Mini Courier Planner is a Python-based courier delivery
optimization system.

It uses different algorithms to prioritize parcels,
optimize bag capacity, find shortest delivery routes,
and generate delivery tours.

## 2. Features

- Parcel prioritization using Sorting.
- Parcel selection using 0/1 Knapsack.
- Shortest path calculation using Dijkstra's Algorithm.
- Delivery tour generation using Nearest Neighbor TSP.
- Performance analysis using Matplotlib.
- CSV report generation and runtime graphs.
- Menu-driven user interface.

## 3. Technologies Used

- Python
- JSON
- Matplotlib
- CSV
- Data Structures and Algorithms

## 4. Project Structure

Mini-Courier-Planner/
- algorithms/
  - sorting.py
  - knapsack.py
  - dijkstra.py
  - tsp.py
- data/
  - parcels.json
  - locations.json
- results/
- main.py
- app.py
- performance.py
- requirements.txt
- README.md

## 5. Installation

Install the required library:

pip install -r requirements.txt

## 6. How to Run

Run the main application:

python app.py

Run performance testing:

python performance.py

## 7. Algorithms Used

1. Sorting Algorithm:
   Prioritizes parcels based on their details.

2. 0/1 Knapsack:
   Selects parcels within the available bag capacity.

3. Dijkstra's Algorithm:
   Finds the shortest path between two locations.

4. Nearest Neighbor TSP:
   Generates a delivery tour using the nearest
   unvisited location.

## 8. Performance Analysis

Performance testing is performed on different
input sizes.

The results are stored in the results folder
as CSV data and PNG graphs.

## 9. Conclusion

The project demonstrates how Data Structures
and Algorithms can be applied to courier
delivery planning and route optimization.
