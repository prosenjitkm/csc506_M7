"""
Graph implementation using Adjacency Matrix representation.
This representation uses a 2D matrix where matrix[i][j] represents
the edge weight between vertex i and vertex j.
"""


class GraphAdjacencyMatrix:
    """
    Graph implementation using adjacency matrix representation.
    Suitable for dense graphs where edge lookup is frequent.

    Time Complexity:
    - Add vertex: O(V²) - needs to resize matrix
    - Add edge: O(1)
    - Remove edge: O(1)
    - Check edge: O(1)
    - Get neighbors: O(V)

    Space Complexity: O(V²)
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
        self.vertices = []  # List to map indices to vertex labels
        self.matrix = []    # Adjacency matrix
        self.vertex_map = {}  # Map vertex labels to indices

    def add_vertex(self, vertex):
        """
        Add a vertex to the graph.

        Args:
            vertex: The vertex label to add

        Returns:
            bool: True if vertex was added, False if it already exists
        """
        if vertex in self.vertex_map:
            return False

        # Add vertex to the list
        self.vertices.append(vertex)
        index = len(self.vertices) - 1
        self.vertex_map[vertex] = index

        # Expand the matrix
        # Add a new row
        self.matrix.append([0] * len(self.vertices))

        # Add a new column to all existing rows
        for i in range(len(self.matrix) - 1):
            self.matrix[i].append(0)

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
        if from_vertex not in self.vertex_map or to_vertex not in self.vertex_map:
            return False

        from_idx = self.vertex_map[from_vertex]
        to_idx = self.vertex_map[to_vertex]

        # Add edge
        self.matrix[from_idx][to_idx] = weight

        # If undirected, add reverse edge
        if not self.directed:
            self.matrix[to_idx][from_idx] = weight

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
        if from_vertex not in self.vertex_map or to_vertex not in self.vertex_map:
            return False

        from_idx = self.vertex_map[from_vertex]
        to_idx = self.vertex_map[to_vertex]

        # Remove edge
        self.matrix[from_idx][to_idx] = 0

        # If undirected, remove reverse edge
        if not self.directed:
            self.matrix[to_idx][from_idx] = 0

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
        if from_vertex not in self.vertex_map or to_vertex not in self.vertex_map:
            return False

        from_idx = self.vertex_map[from_vertex]
        to_idx = self.vertex_map[to_vertex]

        return self.matrix[from_idx][to_idx] != 0

    def get_edge_weight(self, from_vertex, to_vertex):
        """
        Get the weight of an edge between two vertices.

        Args:
            from_vertex: Source vertex
            to_vertex: Destination vertex

        Returns:
            int/float: Edge weight, or None if edge doesn't exist
        """
        if not self.has_edge(from_vertex, to_vertex):
            return None

        from_idx = self.vertex_map[from_vertex]
        to_idx = self.vertex_map[to_vertex]

        return self.matrix[from_idx][to_idx]

    def get_neighbors(self, vertex):
        """
        Get all neighbors of a vertex.

        Args:
            vertex: The vertex to get neighbors for

        Returns:
            list: List of (neighbor, weight) tuples
        """
        if vertex not in self.vertex_map:
            return []

        vertex_idx = self.vertex_map[vertex]
        neighbors = []

        for i, weight in enumerate(self.matrix[vertex_idx]):
            if weight != 0:
                neighbors.append((self.vertices[i], weight))

        return neighbors

    def get_vertices(self):
        """
        Get all vertices in the graph.

        Returns:
            list: List of all vertices
        """
        return self.vertices.copy()

    def get_vertex_count(self):
        """
        Get the number of vertices in the graph.

        Returns:
            int: Number of vertices
        """
        return len(self.vertices)

    def get_edge_count(self):
        """
        Get the number of edges in the graph.

        Returns:
            int: Number of edges
        """
        count = 0
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                if self.matrix[i][j] != 0:
                    count += 1

        # For undirected graphs, each edge is counted twice
        if not self.directed:
            count //= 2

        return count

    def display(self):
        """
        Display the adjacency matrix representation of the graph.
        """
        print("\n" + "="*60)
        print("ADJACENCY MATRIX REPRESENTATION")
        print("="*60)
        print(f"Type: {'Directed' if self.directed else 'Undirected'}, "
              f"{'Weighted' if self.weighted else 'Unweighted'}")
        print(f"Vertices: {len(self.vertices)}, Edges: {self.get_edge_count()}")
        print("-"*60)

        if not self.vertices:
            print("Empty graph")
            return

        # Print header
        print(f"{'':>8}", end="")
        for vertex in self.vertices:
            print(f"{str(vertex):>8}", end="")
        print()

        # Print matrix
        for i, vertex in enumerate(self.vertices):
            print(f"{str(vertex):>8}", end="")
            for j in range(len(self.vertices)):
                weight = self.matrix[i][j]
                if weight == 0:
                    print(f"{'·':>8}", end="")
                else:
                    print(f"{weight:>8}", end="")
            print()
        print("="*60 + "\n")

    def __str__(self):
        """String representation of the graph."""
        return f"GraphAdjacencyMatrix(vertices={len(self.vertices)}, edges={self.get_edge_count()})"

