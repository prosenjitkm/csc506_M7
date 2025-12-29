"""
Shortest path algorithms for graphs.
Implements Dijkstra's algorithm and Bellman-Ford algorithm.
"""

import heapq
from collections import deque


class ShortestPath:
    """
    Collection of shortest path algorithms.
    """

    @staticmethod
    def dijkstra(graph, start_vertex, end_vertex=None, verbose=True):
        """
        Find shortest paths from start vertex to all other vertices using Dijkstra's algorithm.
        Works only with non-negative edge weights.

        Time Complexity: O((V + E) log V) with min-heap
        Space Complexity: O(V)

        Args:
            graph: Graph object
            start_vertex: Starting vertex
            end_vertex: Optional ending vertex (if None, finds paths to all vertices)
            verbose: Whether to print step-by-step output

        Returns:
            tuple: (distances dict, predecessors dict) where distances[v] is the shortest
                   distance from start to v, and predecessors[v] is the previous vertex
        """
        if start_vertex not in graph.get_vertices():
            if verbose:
                print(f"Error: Start vertex '{start_vertex}' not in graph")
            return {}, {}

        # Initialize distances and predecessors
        distances = {v: float('inf') for v in graph.get_vertices()}
        predecessors = {v: None for v in graph.get_vertices()}
        distances[start_vertex] = 0

        # Priority queue: (distance, vertex)
        pq = [(0, start_vertex)]
        visited = set()
        step = 0

        if verbose:
            print("\n" + "="*70)
            print("DIJKSTRA'S SHORTEST PATH ALGORITHM")
            print("="*70)
            print(f"Starting vertex: {start_vertex}")
            if end_vertex:
                print(f"Target vertex: {end_vertex}")
            print("-"*70)

        while pq:
            current_distance, current_vertex = heapq.heappop(pq)

            # Skip if already visited
            if current_vertex in visited:
                continue

            visited.add(current_vertex)
            step += 1

            if verbose:
                print(f"\nStep {step}: Processing vertex {current_vertex}")
                print(f"  Current distance: {current_distance}")

            # If we reached the target, we can stop (optional optimization)
            if end_vertex and current_vertex == end_vertex:
                if verbose:
                    print(f"  Reached target vertex!")
                break

            # Check all neighbors
            neighbors = graph.get_neighbors(current_vertex)
            if verbose and neighbors:
                print(f"  Neighbors: {[(n, w) for n, w in neighbors]}")

            for neighbor, weight in neighbors:
                if neighbor in visited:
                    continue

                # Calculate new distance
                new_distance = current_distance + weight

                # If new distance is shorter, update
                if new_distance < distances[neighbor]:
                    old_distance = distances[neighbor]
                    distances[neighbor] = new_distance
                    predecessors[neighbor] = current_vertex
                    heapq.heappush(pq, (new_distance, neighbor))

                    if verbose:
                        print(f"    {neighbor}: {old_distance} -> {new_distance} "
                              f"(via {current_vertex})")

        if verbose:
            print("\n" + "-"*70)
            print("RESULTS:")
            print("-"*70)

            # Sort vertices for consistent display
            sorted_vertices = sorted([v for v in graph.get_vertices() if v != start_vertex],
                                   key=str)

            print(f"{'Vertex':<15} {'Distance':<15} {'Path':<30}")
            print("-"*70)

            for vertex in [start_vertex] + sorted_vertices:
                if distances[vertex] == float('inf'):
                    print(f"{str(vertex):<15} {'∞':<15} {'No path':<30}")
                else:
                    path = ShortestPath._reconstruct_path(predecessors, start_vertex, vertex)
                    path_str = ' -> '.join(map(str, path))
                    print(f"{str(vertex):<15} {distances[vertex]:<15} {path_str:<30}")

            print("="*70 + "\n")

        return distances, predecessors

    @staticmethod
    def bellman_ford(graph, start_vertex, verbose=True):
        """
        Find shortest paths from start vertex to all other vertices using Bellman-Ford algorithm.
        Works with negative edge weights and detects negative cycles.

        Time Complexity: O(V * E)
        Space Complexity: O(V)

        Args:
            graph: Graph object
            start_vertex: Starting vertex
            verbose: Whether to print step-by-step output

        Returns:
            tuple: (distances dict, predecessors dict, has_negative_cycle bool)
        """
        if start_vertex not in graph.get_vertices():
            if verbose:
                print(f"Error: Start vertex '{start_vertex}' not in graph")
            return {}, {}, False

        vertices = graph.get_vertices()
        distances = {v: float('inf') for v in vertices}
        predecessors = {v: None for v in vertices}
        distances[start_vertex] = 0

        if verbose:
            print("\n" + "="*70)
            print("BELLMAN-FORD SHORTEST PATH ALGORITHM")
            print("="*70)
            print(f"Starting vertex: {start_vertex}")
            print(f"Number of vertices: {len(vertices)}")
            print("-"*70)

        # Relax edges V-1 times
        for iteration in range(len(vertices) - 1):
            updated = False

            if verbose:
                print(f"\nIteration {iteration + 1}:")

            for vertex in vertices:
                if distances[vertex] == float('inf'):
                    continue

                neighbors = graph.get_neighbors(vertex)
                for neighbor, weight in neighbors:
                    new_distance = distances[vertex] + weight

                    if new_distance < distances[neighbor]:
                        distances[neighbor] = new_distance
                        predecessors[neighbor] = vertex
                        updated = True

                        if verbose:
                            print(f"  {vertex} -> {neighbor}: Update distance to {new_distance}")

            if not updated:
                if verbose:
                    print("  No updates made. Algorithm complete.")
                break

        # Check for negative cycles
        has_negative_cycle = False
        if verbose:
            print("\nChecking for negative cycles...")

        for vertex in vertices:
            if distances[vertex] == float('inf'):
                continue

            neighbors = graph.get_neighbors(vertex)
            for neighbor, weight in neighbors:
                if distances[vertex] + weight < distances[neighbor]:
                    has_negative_cycle = True
                    if verbose:
                        print(f"  Negative cycle detected involving edge {vertex} -> {neighbor}")
                    break

            if has_negative_cycle:
                break

        if not has_negative_cycle and verbose:
            print("  No negative cycles detected.")

        if verbose:
            print("\n" + "-"*70)
            print("RESULTS:")
            print("-"*70)

            sorted_vertices = sorted([v for v in vertices if v != start_vertex], key=str)

            print(f"{'Vertex':<15} {'Distance':<15} {'Path':<30}")
            print("-"*70)

            for vertex in [start_vertex] + sorted_vertices:
                if distances[vertex] == float('inf'):
                    print(f"{str(vertex):<15} {'∞':<15} {'No path':<30}")
                else:
                    path = ShortestPath._reconstruct_path(predecessors, start_vertex, vertex)
                    path_str = ' -> '.join(map(str, path))
                    print(f"{str(vertex):<15} {distances[vertex]:<15} {path_str:<30}")

            print("="*70 + "\n")

        return distances, predecessors, has_negative_cycle

    @staticmethod
    def bfs_shortest_path(graph, start_vertex, end_vertex, verbose=True):
        """
        Find shortest path between two vertices using BFS (unweighted graphs).

        Time Complexity: O(V + E)
        Space Complexity: O(V)

        Args:
            graph: Graph object
            start_vertex: Starting vertex
            end_vertex: Ending vertex
            verbose: Whether to print step-by-step output

        Returns:
            list: Shortest path from start to end, or empty list if no path exists
        """
        if start_vertex not in graph.get_vertices() or end_vertex not in graph.get_vertices():
            return []

        if start_vertex == end_vertex:
            return [start_vertex]

        visited = {start_vertex}
        queue = deque([(start_vertex, [start_vertex])])
        step = 0

        if verbose:
            print("\n" + "="*60)
            print("BFS SHORTEST PATH (UNWEIGHTED)")
            print("="*60)
            print(f"From: {start_vertex} -> To: {end_vertex}")
            print("-"*60)

        while queue:
            vertex, path = queue.popleft()
            step += 1

            if verbose:
                print(f"Step {step}: Exploring {vertex}, Path: {' -> '.join(map(str, path))}")

            neighbors = graph.get_neighbors(vertex)
            for neighbor, weight in neighbors:
                if neighbor == end_vertex:
                    final_path = path + [neighbor]
                    if verbose:
                        print(f"\nFound shortest path!")
                        print(f"Path: {' -> '.join(map(str, final_path))}")
                        print(f"Length: {len(final_path) - 1} edges")
                        print("="*60 + "\n")
                    return final_path

                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, path + [neighbor]))

        if verbose:
            print(f"\nNo path found from {start_vertex} to {end_vertex}")
            print("="*60 + "\n")

        return []

    @staticmethod
    def _reconstruct_path(predecessors, start_vertex, end_vertex):
        """
        Reconstruct path from start to end using predecessors dictionary.

        Args:
            predecessors: Dictionary mapping vertex to its predecessor
            start_vertex: Starting vertex
            end_vertex: Ending vertex

        Returns:
            list: Path from start to end
        """
        if predecessors[end_vertex] is None and end_vertex != start_vertex:
            return []

        path = []
        current = end_vertex

        while current is not None:
            path.append(current)
            current = predecessors[current]

        path.reverse()
        return path

    @staticmethod
    def get_path(predecessors, start_vertex, end_vertex):
        """
        Public method to get path from predecessors dictionary.

        Args:
            predecessors: Dictionary from dijkstra or bellman_ford
            start_vertex: Starting vertex
            end_vertex: Ending vertex

        Returns:
            list: Path from start to end
        """
        return ShortestPath._reconstruct_path(predecessors, start_vertex, end_vertex)

