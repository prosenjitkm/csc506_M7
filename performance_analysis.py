"""
Performance analysis and comparison between different graph representations.
"""

import time
import random
from graph_adjacency_matrix import GraphAdjacencyMatrix
from graph_adjacency_list import GraphAdjacencyList


class PerformanceAnalysis:
    """
    Tools for analyzing and comparing performance of different graph representations.
    """

    @staticmethod
    def measure_time(func, *args, **kwargs):
        """Measure execution time of a function."""
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        return result, end - start

    @staticmethod
    def compare_representations(num_vertices=100, num_edges=500, weighted=True, directed=False):
        """
        Compare performance between adjacency matrix and adjacency list representations.

        Args:
            num_vertices: Number of vertices to create
            num_edges: Number of edges to create
            weighted: Whether graph is weighted
            directed: Whether graph is directed
        """
        print("\n" + "="*80)
        print("PERFORMANCE COMPARISON: ADJACENCY MATRIX vs ADJACENCY LIST")
        print("="*80)
        print(f"Test Configuration:")
        print(f"  Vertices: {num_vertices}")
        print(f"  Edges: {num_edges}")
        print(f"  Type: {'Directed' if directed else 'Undirected'}, "
              f"{'Weighted' if weighted else 'Unweighted'}")
        print("-"*80)

        # Create graphs
        matrix_graph = GraphAdjacencyMatrix(directed=directed, weighted=weighted)
        list_graph = GraphAdjacencyList(directed=directed, weighted=weighted)

        # Test 1: Adding vertices
        print("\n1. ADDING VERTICES")
        print("-"*80)

        vertices = [i for i in range(num_vertices)]

        _, matrix_time = PerformanceAnalysis.measure_time(
            lambda: [matrix_graph.add_vertex(v) for v in vertices]
        )
        print(f"Adjacency Matrix: {matrix_time*1000:.4f} ms")

        _, list_time = PerformanceAnalysis.measure_time(
            lambda: [list_graph.add_vertex(v) for v in vertices]
        )
        print(f"Adjacency List:   {list_time*1000:.4f} ms")

        speedup = matrix_time / list_time if list_time > 0 else float('inf')
        print(f"List is {speedup:.2f}x faster")

        # Test 2: Adding edges
        print("\n2. ADDING EDGES")
        print("-"*80)

        # Generate random edges
        edges = []
        edge_set = set()
        while len(edges) < num_edges:
            u = random.randint(0, num_vertices - 1)
            v = random.randint(0, num_vertices - 1)
            if u != v and (u, v) not in edge_set:
                weight = random.randint(1, 100) if weighted else 1
                edges.append((u, v, weight))
                edge_set.add((u, v))
                if not directed:
                    edge_set.add((v, u))

        _, matrix_time = PerformanceAnalysis.measure_time(
            lambda: [matrix_graph.add_edge(u, v, w) for u, v, w in edges]
        )
        print(f"Adjacency Matrix: {matrix_time*1000:.4f} ms")

        _, list_time = PerformanceAnalysis.measure_time(
            lambda: [list_graph.add_edge(u, v, w) for u, v, w in edges]
        )
        print(f"Adjacency List:   {list_time*1000:.4f} ms")

        speedup = matrix_time / list_time if list_time > 0 else float('inf')
        if speedup > 1:
            print(f"List is {speedup:.2f}x faster")
        else:
            print(f"Matrix is {1/speedup:.2f}x faster")

        # Test 3: Checking edges
        print("\n3. CHECKING EDGE EXISTENCE (1000 random checks)")
        print("-"*80)

        test_edges = [(random.randint(0, num_vertices - 1),
                      random.randint(0, num_vertices - 1))
                     for _ in range(1000)]

        _, matrix_time = PerformanceAnalysis.measure_time(
            lambda: [matrix_graph.has_edge(u, v) for u, v in test_edges]
        )
        print(f"Adjacency Matrix: {matrix_time*1000:.4f} ms")

        _, list_time = PerformanceAnalysis.measure_time(
            lambda: [list_graph.has_edge(u, v) for u, v in test_edges]
        )
        print(f"Adjacency List:   {list_time*1000:.4f} ms")

        speedup = list_time / matrix_time if matrix_time > 0 else float('inf')
        if speedup > 1:
            print(f"Matrix is {speedup:.2f}x faster")
        else:
            print(f"List is {1/speedup:.2f}x faster")

        # Test 4: Getting neighbors
        print("\n4. GETTING NEIGHBORS (all vertices)")
        print("-"*80)

        _, matrix_time = PerformanceAnalysis.measure_time(
            lambda: [matrix_graph.get_neighbors(v) for v in vertices]
        )
        print(f"Adjacency Matrix: {matrix_time*1000:.4f} ms")

        _, list_time = PerformanceAnalysis.measure_time(
            lambda: [list_graph.get_neighbors(v) for v in vertices]
        )
        print(f"Adjacency List:   {list_time*1000:.4f} ms")

        speedup = matrix_time / list_time if list_time > 0 else float('inf')
        if speedup > 1:
            print(f"List is {speedup:.2f}x faster")
        else:
            print(f"Matrix is {1/speedup:.2f}x faster")

        # Memory comparison
        print("\n5. MEMORY USAGE (Theoretical)")
        print("-"*80)

        matrix_memory = num_vertices * num_vertices * 8  # Assuming 8 bytes per number
        list_memory = num_vertices * 8 + num_edges * 2 * 8 * (2 if not directed else 1)

        print(f"Adjacency Matrix: ~{matrix_memory / 1024:.2f} KB")
        print(f"Adjacency List:   ~{list_memory / 1024:.2f} KB")
        print(f"List uses {(1 - list_memory/matrix_memory)*100:.1f}% less memory")

        # Summary
        print("\n" + "="*80)
        print("SUMMARY")
        print("="*80)
        print("Adjacency Matrix:")
        print("  + Fast edge existence checks: O(1)")
        print("  + Simple implementation")
        print("  - High memory usage: O(V²)")
        print("  - Slow vertex addition: O(V²)")
        print("  - Slow neighbor iteration for sparse graphs")
        print()
        print("Adjacency List:")
        print("  + Memory efficient for sparse graphs: O(V + E)")
        print("  + Fast vertex addition: O(1)")
        print("  + Fast neighbor iteration: O(degree)")
        print("  - Slower edge existence checks: O(degree)")
        print()
        print("Recommendation:")
        density = num_edges / (num_vertices * (num_vertices - 1) / 2)
        if density > 0.5:
            print("  -> Use ADJACENCY MATRIX for dense graphs (>50% edges)")
        else:
            print("  -> Use ADJACENCY LIST for sparse graphs (<50% edges)")
        print(f"  -> Current graph density: {density*100:.1f}%")
        print("="*80 + "\n")

        return matrix_graph, list_graph

    @staticmethod
    def analyze_graph_properties(graph, name="Graph"):
        """
        Analyze and display properties of a graph.

        Args:
            graph: Graph object to analyze
            name: Name for display
        """
        print("\n" + "="*60)
        print(f"GRAPH ANALYSIS: {name}")
        print("="*60)

        vertices = graph.get_vertices()
        num_vertices = len(vertices)
        num_edges = graph.get_edge_count()

        print(f"Vertices: {num_vertices}")
        print(f"Edges: {num_edges}")
        print(f"Type: {'Directed' if graph.directed else 'Undirected'}")

        if num_vertices == 0:
            print("Empty graph")
            print("="*60 + "\n")
            return

        # Calculate density
        max_edges = num_vertices * (num_vertices - 1)
        if not graph.directed:
            max_edges //= 2
        density = num_edges / max_edges if max_edges > 0 else 0
        print(f"Density: {density*100:.2f}%")

        # Calculate degree statistics
        degrees = []
        for vertex in vertices:
            degree = len(graph.get_neighbors(vertex))
            degrees.append(degree)

        if degrees:
            avg_degree = sum(degrees) / len(degrees)
            max_degree = max(degrees)
            min_degree = min(degrees)

            print(f"\nDegree Statistics:")
            print(f"  Average: {avg_degree:.2f}")
            print(f"  Maximum: {max_degree}")
            print(f"  Minimum: {min_degree}")

            # Find vertices with max degree
            max_degree_vertices = [vertices[i] for i, d in enumerate(degrees) if d == max_degree]
            print(f"  Highest degree vertices: {max_degree_vertices[:5]}")

        # Classify graph
        print(f"\nClassification:")
        if density > 0.7:
            print("  -> Dense graph")
        elif density > 0.3:
            print("  -> Medium density graph")
        else:
            print("  -> Sparse graph")

        print("="*60 + "\n")

