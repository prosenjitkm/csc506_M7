"""
Graph traversal algorithms: Depth-First Search (DFS) and Breadth-First Search (BFS).
These algorithms work with both adjacency matrix and adjacency list representations.
"""

from collections import deque


class GraphTraversal:
    """
    Collection of graph traversal algorithms with step-by-step output.
    """

    @staticmethod
    def depth_first_search(graph, start_vertex, verbose=True):
        """
        Perform depth-first search starting from a given vertex.
        DFS explores as far as possible along each branch before backtracking.

        Time Complexity: O(V + E) for adjacency list, O(V²) for adjacency matrix
        Space Complexity: O(V) for the stack and visited set

        Args:
            graph: Graph object (adjacency matrix or list)
            start_vertex: Starting vertex for traversal
            verbose: Whether to print step-by-step output

        Returns:
            list: List of vertices in DFS order
        """
        if start_vertex not in graph.get_vertices():
            if verbose:
                print(f"Error: Start vertex '{start_vertex}' not in graph")
            return []

        visited = set()
        traversal_order = []
        stack = [start_vertex]
        step = 0

        if verbose:
            print("\n" + "="*60)
            print("DEPTH-FIRST SEARCH (DFS)")
            print("="*60)
            print(f"Starting vertex: {start_vertex}")
            print(f"Graph type: {type(graph).__name__}")
            print("-"*60)

        while stack:
            vertex = stack.pop()

            if vertex not in visited:
                visited.add(vertex)
                traversal_order.append(vertex)
                step += 1

                if verbose:
                    print(f"Step {step}: Visit {vertex}")
                    print(f"  Stack before: {stack}")

                # Get neighbors and add to stack in reverse order
                # (so they are processed in the correct order when popped)
                neighbors = graph.get_neighbors(vertex)
                # Sort neighbors to ensure consistent ordering
                neighbors_sorted = sorted([(n, w) for n, w in neighbors],
                                        key=lambda x: str(x[0]), reverse=True)

                unvisited_neighbors = []
                for neighbor, weight in neighbors_sorted:
                    if neighbor not in visited:
                        stack.append(neighbor)
                        unvisited_neighbors.append(neighbor)

                if verbose:
                    print(f"  Neighbors: {[n for n, _ in neighbors]}")
                    print(f"  Added to stack: {unvisited_neighbors}")
                    print(f"  Stack after: {stack}")
                    print(f"  Visited so far: {traversal_order}")
                    print()

        if verbose:
            print(f"DFS Complete!")
            print(f"Traversal order: {' -> '.join(map(str, traversal_order))}")
            print(f"Vertices visited: {len(traversal_order)} / {graph.get_vertex_count()}")
            print("="*60 + "\n")

        return traversal_order

    @staticmethod
    def depth_first_search_recursive(graph, start_vertex, visited=None,
                                     traversal_order=None, verbose=True, step_counter=None):
        """
        Perform depth-first search recursively.

        Args:
            graph: Graph object (adjacency matrix or list)
            start_vertex: Starting vertex for traversal
            visited: Set of visited vertices
            traversal_order: List to store traversal order
            verbose: Whether to print step-by-step output
            step_counter: List with one element to track step number

        Returns:
            list: List of vertices in DFS order
        """
        # Initialize on first call
        if visited is None:
            visited = set()
            traversal_order = []
            step_counter = [0]

            if verbose:
                print("\n" + "="*60)
                print("DEPTH-FIRST SEARCH (DFS) - RECURSIVE")
                print("="*60)
                print(f"Starting vertex: {start_vertex}")
                print(f"Graph type: {type(graph).__name__}")
                print("-"*60)

        if start_vertex not in graph.get_vertices():
            return traversal_order

        # Visit current vertex
        visited.add(start_vertex)
        traversal_order.append(start_vertex)
        step_counter[0] += 1

        if verbose:
            print(f"Step {step_counter[0]}: Visit {start_vertex}")

        # Get and sort neighbors for consistent ordering
        neighbors = graph.get_neighbors(start_vertex)
        neighbors_sorted = sorted([(n, w) for n, w in neighbors], key=lambda x: str(x[0]))

        if verbose:
            print(f"  Neighbors: {[n for n, _ in neighbors]}")

        # Recursively visit unvisited neighbors
        for neighbor, weight in neighbors_sorted:
            if neighbor not in visited:
                if verbose:
                    print(f"  Recursing into {neighbor}")
                GraphTraversal.depth_first_search_recursive(
                    graph, neighbor, visited, traversal_order, verbose, step_counter
                )

        # Print completion on final return
        if len(visited) == len(traversal_order) and step_counter[0] == len(traversal_order):
            if verbose:
                print(f"\nDFS Complete!")
                print(f"Traversal order: {' -> '.join(map(str, traversal_order))}")
                print(f"Vertices visited: {len(traversal_order)} / {graph.get_vertex_count()}")
                print("="*60 + "\n")

        return traversal_order

    @staticmethod
    def breadth_first_search(graph, start_vertex, verbose=True):
        """
        Perform breadth-first search starting from a given vertex.
        BFS explores all neighbors at the present depth before moving to vertices at the next depth.

        Time Complexity: O(V + E) for adjacency list, O(V²) for adjacency matrix
        Space Complexity: O(V) for the queue and visited set

        Args:
            graph: Graph object (adjacency matrix or list)
            start_vertex: Starting vertex for traversal
            verbose: Whether to print step-by-step output

        Returns:
            list: List of vertices in BFS order
        """
        if start_vertex not in graph.get_vertices():
            if verbose:
                print(f"Error: Start vertex '{start_vertex}' not in graph")
            return []

        visited = set()
        traversal_order = []
        queue = deque([start_vertex])
        visited.add(start_vertex)
        step = 0

        if verbose:
            print("\n" + "="*60)
            print("BREADTH-FIRST SEARCH (BFS)")
            print("="*60)
            print(f"Starting vertex: {start_vertex}")
            print(f"Graph type: {type(graph).__name__}")
            print("-"*60)

        while queue:
            vertex = queue.popleft()
            traversal_order.append(vertex)
            step += 1

            if verbose:
                print(f"Step {step}: Visit {vertex}")
                print(f"  Queue before: {list(queue)}")

            # Get neighbors
            neighbors = graph.get_neighbors(vertex)
            # Sort neighbors for consistent ordering
            neighbors_sorted = sorted([(n, w) for n, w in neighbors], key=lambda x: str(x[0]))

            added_neighbors = []
            for neighbor, weight in neighbors_sorted:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
                    added_neighbors.append(neighbor)

            if verbose:
                print(f"  Neighbors: {[n for n, _ in neighbors]}")
                print(f"  Added to queue: {added_neighbors}")
                print(f"  Queue after: {list(queue)}")
                print(f"  Visited so far: {traversal_order}")
                print()

        if verbose:
            print(f"BFS Complete!")
            print(f"Traversal order: {' -> '.join(map(str, traversal_order))}")
            print(f"Vertices visited: {len(traversal_order)} / {graph.get_vertex_count()}")
            print("="*60 + "\n")

        return traversal_order

    @staticmethod
    def find_all_paths(graph, start_vertex, end_vertex, max_paths=10, verbose=True):
        """
        Find all paths between two vertices using DFS.

        Args:
            graph: Graph object
            start_vertex: Starting vertex
            end_vertex: Ending vertex
            max_paths: Maximum number of paths to find
            verbose: Whether to print output

        Returns:
            list: List of paths, where each path is a list of vertices
        """
        if start_vertex not in graph.get_vertices() or end_vertex not in graph.get_vertices():
            return []

        all_paths = []

        def dfs_paths(current, target, path, visited):
            if len(all_paths) >= max_paths:
                return

            if current == target:
                all_paths.append(path.copy())
                return

            neighbors = graph.get_neighbors(current)
            for neighbor, weight in neighbors:
                if neighbor not in visited:
                    visited.add(neighbor)
                    path.append(neighbor)
                    dfs_paths(neighbor, target, path, visited)
                    path.pop()
                    visited.remove(neighbor)

        visited = {start_vertex}
        dfs_paths(start_vertex, end_vertex, [start_vertex], visited)

        if verbose:
            print("\n" + "="*60)
            print(f"ALL PATHS FROM {start_vertex} TO {end_vertex}")
            print("="*60)
            if all_paths:
                for i, path in enumerate(all_paths, 1):
                    print(f"Path {i}: {' -> '.join(map(str, path))}")
            else:
                print(f"No path found from {start_vertex} to {end_vertex}")
            print("="*60 + "\n")

        return all_paths

    @staticmethod
    def is_connected(graph, verbose=True):
        """
        Check if the graph is connected (all vertices are reachable from any vertex).
        For directed graphs, checks weak connectivity.

        Args:
            graph: Graph object
            verbose: Whether to print output

        Returns:
            bool: True if graph is connected
        """
        vertices = graph.get_vertices()
        if not vertices:
            return True

        # Start DFS from first vertex
        visited = GraphTraversal.depth_first_search(graph, vertices[0], verbose=False)

        is_connected = len(visited) == len(vertices)

        if verbose:
            print(f"\nGraph connectivity: {'Connected' if is_connected else 'Disconnected'}")
            print(f"Reachable vertices: {len(visited)} / {len(vertices)}")
            if not is_connected:
                unreachable = set(vertices) - set(visited)
                print(f"Unreachable vertices: {unreachable}")

        return is_connected

