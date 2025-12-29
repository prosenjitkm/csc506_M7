"""
Graph implementation using Adjacency List representation.
This representation uses a dictionary where each vertex maps to a list
of its adjacent vertices and edge weights.
"""


class GraphAdjacencyList:
    """
    Graph implementation using adjacency list representation.
    Suitable for sparse graphs where memory efficiency is important.

    Time Complexity:
    - Add vertex: O(1)
    - Add edge: O(1)
    - Remove edge: O(E) where E is edges from vertex
    - Check edge: O(E) where E is edges from vertex
    - Get neighbors: O(1)

    Space Complexity: O(V + E)
    """

    def __init__(self, directed=False, weighted=False):
        """
        Initialize the graph.

        Args:
            directed (bool): Whether the graph is directed
            weighted (bool): Whether the graph is weighted
        """
        self.directed = directed
        self.weighted = weighted
        self.adjacency_list = {}  # Maps vertex -> list of (neighbor, weight) tuples

    def add_vertex(self, vertex):
        """
        Add a vertex to the graph.

        Args:
            vertex: The vertex label to add

        Returns:
            bool: True if vertex was added, False if it already exists
        """
        if vertex in self.adjacency_list:
            return False

        self.adjacency_list[vertex] = []
        return True

    def add_edge(self, from_vertex, to_vertex, weight=1):
        """
        Add an edge between two vertices.

        Args:
            from_vertex: Source vertex
            to_vertex: Destination vertex
            weight: Edge weight (default 1 for unweighted graphs)

        Returns:
            bool: True if edge was added, False if vertices don't exist
        """
        if from_vertex not in self.adjacency_list or to_vertex not in self.adjacency_list:
            return False

        # Check if edge already exists, update weight if it does
        for i, (neighbor, _) in enumerate(self.adjacency_list[from_vertex]):
            if neighbor == to_vertex:
                self.adjacency_list[from_vertex][i] = (to_vertex, weight)
                if not self.directed:
                    for j, (neighbor2, _) in enumerate(self.adjacency_list[to_vertex]):
                        if neighbor2 == from_vertex:
                            self.adjacency_list[to_vertex][j] = (from_vertex, weight)
                return True

        # Add new edge
        self.adjacency_list[from_vertex].append((to_vertex, weight))

        # If undirected, add reverse edge
        if not self.directed:
            self.adjacency_list[to_vertex].append((from_vertex, weight))

        return True

    def remove_edge(self, from_vertex, to_vertex):
        """
        Remove an edge between two vertices.

        Args:
            from_vertex: Source vertex
            to_vertex: Destination vertex

        Returns:
            bool: True if edge was removed, False if vertices don't exist
        """
        if from_vertex not in self.adjacency_list or to_vertex not in self.adjacency_list:
            return False

        # Remove edge from adjacency list
        self.adjacency_list[from_vertex] = [
            (neighbor, weight) for neighbor, weight in self.adjacency_list[from_vertex]
            if neighbor != to_vertex
        ]

        # If undirected, remove reverse edge
        if not self.directed:
            self.adjacency_list[to_vertex] = [
                (neighbor, weight) for neighbor, weight in self.adjacency_list[to_vertex]
                if neighbor != from_vertex
            ]

        return True

    def has_edge(self, from_vertex, to_vertex):
        """
        Check if an edge exists between two vertices.

        Args:
            from_vertex: Source vertex
            to_vertex: Destination vertex

        Returns:
            bool: True if edge exists, False otherwise
        """
        if from_vertex not in self.adjacency_list:
            return False

        for neighbor, _ in self.adjacency_list[from_vertex]:
            if neighbor == to_vertex:
                return True

        return False

    def get_edge_weight(self, from_vertex, to_vertex):
        """
        Get the weight of an edge between two vertices.

        Args:
            from_vertex: Source vertex
            to_vertex: Destination vertex

        Returns:
            int/float: Edge weight, or None if edge doesn't exist
        """
        if from_vertex not in self.adjacency_list:
            return None

        for neighbor, weight in self.adjacency_list[from_vertex]:
            if neighbor == to_vertex:
                return weight

        return None

    def get_neighbors(self, vertex):
        """
        Get all neighbors of a vertex.

        Args:
            vertex: The vertex to get neighbors for

        Returns:
            list: List of (neighbor, weight) tuples
        """
        if vertex not in self.adjacency_list:
            return []

        return self.adjacency_list[vertex].copy()

    def get_vertices(self):
        """
        Get all vertices in the graph.

        Returns:
            list: List of all vertices
        """
        return list(self.adjacency_list.keys())

    def get_vertex_count(self):
        """
        Get the number of vertices in the graph.

        Returns:
            int: Number of vertices
        """
        return len(self.adjacency_list)

    def get_edge_count(self):
        """
        Get the number of edges in the graph.

        Returns:
            int: Number of edges
        """
        count = 0
        for neighbors in self.adjacency_list.values():
            count += len(neighbors)

        # For undirected graphs, each edge is counted twice
        if not self.directed:
            count //= 2

        return count

    def display(self):
        """
        Display the adjacency list representation of the graph.
        """
        print("\n" + "="*60)
        print("ADJACENCY LIST REPRESENTATION")
        print("="*60)
        print(f"Type: {'Directed' if self.directed else 'Undirected'}, "
              f"{'Weighted' if self.weighted else 'Unweighted'}")
        print(f"Vertices: {len(self.adjacency_list)}, Edges: {self.get_edge_count()}")
        print("-"*60)

        if not self.adjacency_list:
            print("Empty graph")
            return

        # Sort vertices for consistent display
        vertices = sorted(self.adjacency_list.keys(), key=str)

        for vertex in vertices:
            neighbors = self.adjacency_list[vertex]
            if neighbors:
                neighbor_strs = [f"{n}({w})" if self.weighted else str(n)
                               for n, w in neighbors]
                print(f"{vertex:>8} -> {', '.join(neighbor_strs)}")
            else:
                print(f"{vertex:>8} -> (no edges)")

        print("="*60 + "\n")

    def __str__(self):
        """String representation of the graph."""
        return f"GraphAdjacencyList(vertices={len(self.adjacency_list)}, edges={self.get_edge_count()})"

