# City Path Finder

This is an interactive program where the user chooses two cities from the cities.csv file and then chooses the search algorithm, either breadth-first search or depth-first search, for finding a valid path between the two cities.

## Program Structure

The program consists of the following components:

1. **Cities Graph**: The cities are implemented as a graph, where the city name is the vertex and the edges are a list of
other cities connected to it.

2. **Search Algorithms Implementation**:
   - Depth-First Search (DFS): Explores as far as possible along each branch before backtracking.
   - Breadth-First Search (BFS): Explores all neighbor nodes at the present depth before moving on to the nodes at the next depth level.

3. **Graph**: An undirected graph with generic vertices and edges connecting vertices.

4. **Node**: A node represents attributes for state, parent, cost, and heuristic.

5. **Stack**: A LIFO data structure used for depth-first search.

6. **Queue**: A FIFO data structure used for breadth-first search.

## How to Use

1. **Input**: Provide the program a departing city and arrival city.

2. **Choose the search algorithm**: At this point there are only two search algorithms to choose from:
    1. Breadth-first search
    2. Depth-first search

3. **Output**: The program outputs the path found by the search algorithm.

Example:
```
Enter city departure: new york
Enter city destination: san francisco

Choose one of the options below

 1. Use breadth-first search

 2. Use depth-first search 

 3. To quit program.

 Enter choice: 1

Found path using breadth-first search
['New York', 'Detroit', 'Chicago', 'Seattle', 'San Francisco']
```