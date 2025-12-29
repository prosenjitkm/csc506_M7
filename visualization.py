"""
Visualization tools for graphs and their traversal/shortest path algorithms.
Creates ASCII art representations and step-by-step visual outputs.
"""


class GraphVisualizer:
    """
    Tools for visualizing graphs and algorithm execution.
    """

    @staticmethod
    def visualize_graph(graph, title="Graph Visualization"):
        """
        Create an ASCII visualization of the graph structure.

        Args:
            graph: Graph object to visualize
            title: Title for the visualization
        """
        print("\n" + "="*70)
        print(title.center(70))
        print("="*70)

        vertices = sorted(graph.get_vertices(), key=str)

        if not vertices:
            print("Empty graph")
            print("="*70 + "\n")
            return

        print(f"\nVertices: {', '.join(map(str, vertices))}")
        print(f"Total: {len(vertices)} vertices, {graph.get_edge_count()} edges")
        print("\nEdge List:")
        print("-"*70)

        edges = []
        for vertex in vertices:
            neighbors = graph.get_neighbors(vertex)
            for neighbor, weight in neighbors:
                if graph.directed or str(vertex) <= str(neighbor):  # Avoid duplicates for undirected
                    arrow = "->" if graph.directed else "<->"
                    weight_str = f"[{weight}]" if graph.weighted else ""
                    edges.append(f"{vertex} {arrow} {neighbor} {weight_str}")

        if edges:
            for edge in edges:
                print(f"  {edge}")
        else:
            print("  No edges")

        # Create adjacency representation
        print("\nAdjacency Relationships:")
        print("-"*70)
        for vertex in vertices:
            neighbors = graph.get_neighbors(vertex)
            if neighbors:
                neighbor_list = [f"{n}({w})" if graph.weighted else str(n)
                               for n, w in neighbors]
                print(f"  {vertex:>5} -> {{ {', '.join(neighbor_list)} }}")
            else:
                print(f"  {vertex:>5} -> {{ isolated }}")

        print("="*70 + "\n")

    @staticmethod
    def visualize_traversal(graph, traversal_order, algorithm_name, start_vertex):
        """
        Visualize the order of traversal in a graph.

        Args:
            graph: Graph object
            traversal_order: List of vertices in traversal order
            algorithm_name: Name of the algorithm (DFS/BFS)
            start_vertex: Starting vertex
        """
        print("\n" + "="*70)
        print(f"{algorithm_name} TRAVERSAL VISUALIZATION".center(70))
        print("="*70)
        print(f"Start: {start_vertex}")
        print(f"Order: {' -> '.join(map(str, traversal_order))}")
        print("-"*70)

        # Show step-by-step
        print("\nStep-by-Step Visualization:")
        print()

        visited = set()
        for step, vertex in enumerate(traversal_order, 1):
            visited.add(vertex)

            # Create visual representation
            status = []
            for v in sorted(graph.get_vertices(), key=str):
                if v == vertex:
                    status.append(f"[{v}*]")  # Current
                elif v in visited:
                    status.append(f"[{v}+]")  # Visited
                else:
                    status.append(f"[{v} ]")  # Unvisited

            print(f"Step {step:2d}: {' '.join(status)}")
            print(f"         Visiting: {vertex}")

            # Show neighbors
            neighbors = graph.get_neighbors(vertex)
            if neighbors:
                neighbor_names = [str(n) for n, w in neighbors]
                print(f"         Neighbors: {', '.join(neighbor_names)}")
            print()

        print("Legend: [*] = Current, [+] = Visited, [ ] = Unvisited")
        print("="*70 + "\n")

    @staticmethod
    def visualize_shortest_path(graph, start_vertex, end_vertex, path, distance):
        """
        Visualize the shortest path between two vertices.

        Args:
            graph: Graph object
            start_vertex: Starting vertex
            end_vertex: Ending vertex
            path: List of vertices in the shortest path
            distance: Total distance of the path
        """
        print("\n" + "="*70)
        print("SHORTEST PATH VISUALIZATION".center(70))
        print("="*70)
        print(f"From: {start_vertex}")
        print(f"To: {end_vertex}")

        if not path:
            print("\nNo path exists!")
            print("="*70 + "\n")
            return

        print(f"Distance: {distance}")
        print(f"Hops: {len(path) - 1}")
        print("-"*70)

        # Visual path representation
        print("\nPath:")
        print()
        path_str = " -> ".join(map(str, path))
        print(f"  {path_str}")
        print()

        # Detailed breakdown
        print("Detailed Breakdown:")
        print("-"*70)

        cumulative_distance = 0
        for i in range(len(path) - 1):
            u, v = path[i], path[i + 1]
            weight = graph.get_edge_weight(u, v)
            cumulative_distance += weight

            print(f"Step {i+1}: {u} -> {v}")
            print(f"        Edge weight: {weight}")
            print(f"        Cumulative: {cumulative_distance}")
            print()

        # Highlight on graph
        print("Path Highlighted on Graph:")
        print("-"*70)

        path_set = set(path)
        path_edges = set((path[i], path[i+1]) for i in range(len(path) - 1))

        vertices = sorted(graph.get_vertices(), key=str)
        for vertex in vertices:
            if vertex in path_set:
                if vertex == start_vertex:
                    marker = "START"
                elif vertex == end_vertex:
                    marker = "END"
                else:
                    marker = "PATH"
                print(f"  [{vertex}] {marker:>10}", end="")
            else:
                print(f"  [{vertex}] {'':>10}", end="")

            neighbors = graph.get_neighbors(vertex)
            if neighbors:
                neighbor_strs = []
                for neighbor, weight in neighbors:
                    if (vertex, neighbor) in path_edges:
                        neighbor_strs.append(f"-> {neighbor}({weight}) *")
                    else:
                        neighbor_strs.append(f"-> {neighbor}({weight})")
                print(f"  {', '.join(neighbor_strs)}")
            else:
                print()

        print("\n* = Edge on shortest path")
        print("="*70 + "\n")

    @staticmethod
    def visualize_graph_ascii_art(graph, highlight_vertices=None):
        """
        Create a simple ASCII art representation of a small graph.
        Works best for graphs with 10 or fewer vertices.

        Args:
            graph: Graph object
            highlight_vertices: Set of vertices to highlight
        """
        if highlight_vertices is None:
            highlight_vertices = set()

        print("\n" + "="*70)
        print("ASCII ART REPRESENTATION".center(70))
        print("="*70)

        vertices = sorted(graph.get_vertices(), key=str)

        if len(vertices) > 10:
            print("Graph too large for ASCII art (max 10 vertices)")
            print("="*70 + "\n")
            return

        if not vertices:
            print("Empty graph")
            print("="*70 + "\n")
            return

        # Simple circular layout
        print()
        for i, vertex in enumerate(vertices):
            marker = "(*)" if vertex in highlight_vertices else "(·)"
            indent = " " * (i * 7)
            print(f"{indent}{marker} {vertex}")

            # Show connections
            neighbors = graph.get_neighbors(vertex)
            for neighbor, weight in neighbors:
                arrow = "  ->" if graph.directed else "  <->"
                weight_str = f"[{weight}]" if graph.weighted else ""
                print(f"{indent}    {arrow} {neighbor} {weight_str}")
            print()

        print("="*70 + "\n")

    @staticmethod
    def create_distance_table(distances, start_vertex, graph):
        """
        Create a formatted distance table.

        Args:
            distances: Dictionary of distances from start vertex
            start_vertex: The starting vertex
            graph: Graph object
        """
        print("\n" + "="*60)
        print("DISTANCE TABLE".center(60))
        print("="*60)
        print(f"From vertex: {start_vertex}")
        print("-"*60)

        print(f"{'Vertex':<15} {'Distance':<15} {'Status':<15}")
        print("-"*60)

        vertices = sorted([v for v in graph.get_vertices()], key=str)

        for vertex in vertices:
            distance = distances.get(vertex, float('inf'))

            if distance == float('inf'):
                dist_str = "∞"
                status = "Unreachable"
            elif distance == 0:
                dist_str = "0"
                status = "Start"
            else:
                dist_str = str(distance)
                status = "Reachable"

            print(f"{str(vertex):<15} {dist_str:<15} {status:<15}")

        print("="*60 + "\n")

    @staticmethod
    def create_execution_timeline(steps, title="Algorithm Execution Timeline"):
        """
        Create a visual timeline of algorithm execution steps.

        Args:
            steps: List of (step_number, description) tuples
            title: Title for the timeline
        """
        print("\n" + "="*70)
        print(title.center(70))
        print("="*70)

        for step_num, description in steps:
            print(f"\n{'>' if step_num > 0 else 'o'} Step {step_num}: {description}")

        print("\n" + "="*70 + "\n")

