"""
Comprehensive test program demonstrating graph implementations and algorithms.

This program demonstrates:
1. Graph construction with both adjacency matrix and adjacency list
2. Graph manipulation (adding/removing vertices and edges)
3. Graph traversal algorithms (DFS and BFS)
4. Shortest path algorithms (Dijkstra, Bellman-Ford, BFS)
5. Performance analysis comparing representations
6. Visual representations of graphs and algorithm execution
"""

from graph_adjacency_matrix import GraphAdjacencyMatrix
from graph_adjacency_list import GraphAdjacencyList
from graph_traversal import GraphTraversal
from shortest_path import ShortestPath
from performance_analysis import PerformanceAnalysis
from visualization import GraphVisualizer


def demo_basic_operations():
    """Demonstrate basic graph operations."""
    print("\n" + "#"*80)
    print("# DEMO 1: BASIC GRAPH OPERATIONS")
    print("#"*80)

    # Create graphs with both representations
    print("\n>>> Creating graphs with both representations...")
    matrix_graph = GraphAdjacencyMatrix(directed=False, weighted=True)
    list_graph = GraphAdjacencyList(directed=False, weighted=True)

    # Add vertices
    print("\n>>> Adding vertices: A, B, C, D, E")
    vertices = ['A', 'B', 'C', 'D', 'E']
    for v in vertices:
        matrix_graph.add_vertex(v)
        list_graph.add_vertex(v)

    # Add edges
    print(">>> Adding edges with weights")
    edges = [
        ('A', 'B', 4),
        ('A', 'C', 2),
        ('B', 'C', 1),
        ('B', 'D', 5),
        ('C', 'D', 8),
        ('C', 'E', 10),
        ('D', 'E', 2)
    ]

    for u, v, w in edges:
        matrix_graph.add_edge(u, v, w)
        list_graph.add_edge(u, v, w)
        print(f"   Added edge: {u} <-> {v} (weight: {w})")

    # Display both representations
    matrix_graph.display()
    list_graph.display()

    # Visualize
    GraphVisualizer.visualize_graph(matrix_graph, "Undirected Weighted Graph")

    print("\n>>> Testing edge operations...")
    print(f"Has edge A-B? {matrix_graph.has_edge('A', 'B')}")
    print(f"Weight of A-B: {matrix_graph.get_edge_weight('A', 'B')}")
    print(f"Neighbors of C: {matrix_graph.get_neighbors('C')}")

    # Analyze properties
    PerformanceAnalysis.analyze_graph_properties(matrix_graph, "Undirected Weighted Graph")


def demo_directed_graph():
    """Demonstrate directed graph operations."""
    print("\n" + "#"*80)
    print("# DEMO 2: DIRECTED GRAPH")
    print("#"*80)

    print("\n>>> Creating a directed graph (Social Network)")
    graph = GraphAdjacencyList(directed=True, weighted=False)

    # Add users
    users = ['Alice', 'Bob', 'Carol', 'David', 'Eve']
    for user in users:
        graph.add_vertex(user)

    # Add following relationships
    print("\n>>> Adding following relationships (A -> B means A follows B)")
    follows = [
        ('Alice', 'Bob'),
        ('Alice', 'Carol'),
        ('Bob', 'Carol'),
        ('Bob', 'David'),
        ('Carol', 'David'),
        ('Carol', 'Eve'),
        ('David', 'Eve'),
        ('Eve', 'Alice')
    ]

    for u, v in follows:
        graph.add_edge(u, v, 1)
        print(f"   {u} follows {v}")

    graph.display()
    GraphVisualizer.visualize_graph(graph, "Social Network (Directed Graph)")


def demo_traversal_algorithms():
    """Demonstrate graph traversal algorithms."""
    print("\n" + "#"*80)
    print("# DEMO 3: GRAPH TRAVERSAL ALGORITHMS")
    print("#"*80)

    # Create a graph
    print("\n>>> Creating a graph for traversal demonstration")
    graph = GraphAdjacencyList(directed=False, weighted=False)

    vertices = [1, 2, 3, 4, 5, 6, 7, 8]
    for v in vertices:
        graph.add_vertex(v)

    edges = [
        (1, 2), (1, 3),
        (2, 4), (2, 5),
        (3, 6), (3, 7),
        (4, 8), (5, 8)
    ]

    for u, v in edges:
        graph.add_edge(u, v, 1)

    graph.display()
    GraphVisualizer.visualize_graph(graph, "Tree-like Graph for Traversal")

    # Depth-First Search (Iterative)
    print("\n" + "="*80)
    print("DEPTH-FIRST SEARCH (ITERATIVE)")
    print("="*80)
    dfs_order = GraphTraversal.depth_first_search(graph, 1, verbose=True)
    GraphVisualizer.visualize_traversal(graph, dfs_order, "DFS (Iterative)", 1)

    # Depth-First Search (Recursive)
    print("\n" + "="*80)
    print("DEPTH-FIRST SEARCH (RECURSIVE)")
    print("="*80)
    dfs_recursive_order = GraphTraversal.depth_first_search_recursive(graph, 1, verbose=True)

    # Breadth-First Search
    print("\n" + "="*80)
    print("BREADTH-FIRST SEARCH")
    print("="*80)
    bfs_order = GraphTraversal.breadth_first_search(graph, 1, verbose=True)
    GraphVisualizer.visualize_traversal(graph, bfs_order, "BFS", 1)

    # Compare orders
    print("\n" + "="*80)
    print("COMPARISON OF TRAVERSAL ORDERS")
    print("="*80)
    print(f"DFS (Iterative): {' -> '.join(map(str, dfs_order))}")
    print(f"DFS (Recursive): {' -> '.join(map(str, dfs_recursive_order))}")
    print(f"BFS:             {' -> '.join(map(str, bfs_order))}")
    print()
    print("Note: DFS and BFS visit vertices in different orders.")
    print("DFS explores deeply before backtracking, BFS explores level by level.")
    print("="*80)


def demo_shortest_path_algorithms():
    """Demonstrate shortest path algorithms."""
    print("\n" + "#"*80)
    print("# DEMO 4: SHORTEST PATH ALGORITHMS")
    print("#"*80)

    # Create a weighted graph
    print("\n>>> Creating a weighted graph (City Network)")
    graph = GraphAdjacencyList(directed=False, weighted=True)

    cities = ['NYC', 'LA', 'Chicago', 'Houston', 'Phoenix', 'Philadelphia']
    for city in cities:
        graph.add_vertex(city)

    # Add routes with distances
    routes = [
        ('NYC', 'Philadelphia', 95),
        ('NYC', 'Chicago', 790),
        ('LA', 'Phoenix', 370),
        ('LA', 'Houston', 1550),
        ('Chicago', 'Houston', 1080),
        ('Chicago', 'Philadelphia', 760),
        ('Houston', 'Phoenix', 1180),
        ('Phoenix', 'Philadelphia', 2260)
    ]

    for u, v, distance in routes:
        graph.add_edge(u, v, distance)

    graph.display()
    GraphVisualizer.visualize_graph(graph, "City Network with Distances (miles)")

    # Dijkstra's Algorithm
    print("\n" + "="*80)
    print("DIJKSTRA'S ALGORITHM")
    print("="*80)
    start = 'NYC'
    end = 'Phoenix'
    distances, predecessors = ShortestPath.dijkstra(graph, start, end, verbose=True)

    # Visualize shortest path
    path = ShortestPath.get_path(predecessors, start, end)
    if path:
        GraphVisualizer.visualize_shortest_path(graph, start, end, path, distances[end])

    # BFS shortest path (unweighted)
    print("\n>>> Testing BFS shortest path (treats all edges as weight 1)")
    bfs_path = ShortestPath.bfs_shortest_path(graph, start, end, verbose=True)

    # Find all paths
    print("\n>>> Finding all possible paths")
    all_paths = GraphTraversal.find_all_paths(graph, start, end, max_paths=5, verbose=True)


def demo_advanced_scenarios():
    """Demonstrate advanced graph scenarios."""
    print("\n" + "#"*80)
    print("# DEMO 5: ADVANCED SCENARIOS")
    print("#"*80)

    # Scenario 1: Disconnected Graph
    print("\n>>> SCENARIO 1: Disconnected Graph")
    graph = GraphAdjacencyList(directed=False, weighted=False)

    # Component 1
    for v in ['A', 'B', 'C']:
        graph.add_vertex(v)
    graph.add_edge('A', 'B', 1)
    graph.add_edge('B', 'C', 1)

    # Component 2 (disconnected)
    for v in ['X', 'Y', 'Z']:
        graph.add_vertex(v)
    graph.add_edge('X', 'Y', 1)
    graph.add_edge('Y', 'Z', 1)

    graph.display()
    GraphTraversal.is_connected(graph, verbose=True)

    # Scenario 2: Cyclic Graph
    print("\n>>> SCENARIO 2: Cyclic Graph")
    cyclic_graph = GraphAdjacencyList(directed=True, weighted=False)

    for v in [1, 2, 3, 4]:
        cyclic_graph.add_vertex(v)

    cyclic_graph.add_edge(1, 2, 1)
    cyclic_graph.add_edge(2, 3, 1)
    cyclic_graph.add_edge(3, 4, 1)
    cyclic_graph.add_edge(4, 1, 1)  # Cycle

    cyclic_graph.display()
    GraphVisualizer.visualize_graph(cyclic_graph, "Cyclic Directed Graph")

    print("\n>>> Detecting cycle through DFS")
    dfs_order = GraphTraversal.depth_first_search(cyclic_graph, 1, verbose=True)

    # Scenario 3: Complete Graph
    print("\n>>> SCENARIO 3: Complete Graph (K5)")
    complete_graph = GraphAdjacencyMatrix(directed=False, weighted=False)

    vertices = [1, 2, 3, 4, 5]
    for v in vertices:
        complete_graph.add_vertex(v)

    # Add all possible edges
    for i in range(len(vertices)):
        for j in range(i + 1, len(vertices)):
            complete_graph.add_edge(vertices[i], vertices[j], 1)

    complete_graph.display()
    PerformanceAnalysis.analyze_graph_properties(complete_graph, "Complete Graph K5")


def demo_performance_comparison():
    """Demonstrate performance comparison between representations."""
    print("\n" + "#"*80)
    print("# DEMO 6: PERFORMANCE COMPARISON")
    print("#"*80)

    # Test with different graph sizes
    print("\n>>> Test 1: Small Sparse Graph")
    PerformanceAnalysis.compare_representations(
        num_vertices=50,
        num_edges=100,
        weighted=True,
        directed=False
    )

    print("\n>>> Test 2: Medium Dense Graph")
    PerformanceAnalysis.compare_representations(
        num_vertices=100,
        num_edges=2000,
        weighted=True,
        directed=False
    )


def demo_real_world_application():
    """Demonstrate a real-world application: Route Planning System."""
    print("\n" + "#"*80)
    print("# DEMO 7: REAL-WORLD APPLICATION - GPS ROUTE PLANNING")
    print("#"*80)

    print("\n>>> Building a city street network...")

    # Create a detailed city map
    city_map = GraphAdjacencyList(directed=False, weighted=True)

    locations = [
        'Home', 'School', 'Park', 'Mall', 'Hospital',
        'Library', 'Gym', 'Restaurant', 'Office', 'Station'
    ]

    for loc in locations:
        city_map.add_vertex(loc)

    # Add roads with travel times (minutes)
    roads = [
        ('Home', 'School', 5),
        ('Home', 'Park', 10),
        ('School', 'Library', 8),
        ('School', 'Mall', 12),
        ('Park', 'Mall', 7),
        ('Park', 'Restaurant', 6),
        ('Mall', 'Hospital', 15),
        ('Mall', 'Office', 20),
        ('Library', 'Gym', 5),
        ('Library', 'Office', 18),
        ('Hospital', 'Station', 10),
        ('Gym', 'Restaurant', 4),
        ('Restaurant', 'Office', 9),
        ('Office', 'Station', 12)
    ]

    for u, v, time in roads:
        city_map.add_edge(u, v, time)

    city_map.display()
    GraphVisualizer.visualize_graph(city_map, "City Street Network (Travel Times in Minutes)")

    # Find routes
    print("\n" + "="*80)
    print("ROUTE PLANNING: Finding best route from Home to Station")
    print("="*80)

    start = 'Home'
    destination = 'Station'

    # Use Dijkstra to find shortest path
    distances, predecessors = ShortestPath.dijkstra(city_map, start, destination, verbose=True)

    # Get and visualize the route
    route = ShortestPath.get_path(predecessors, start, destination)
    if route:
        travel_time = distances[destination]
        GraphVisualizer.visualize_shortest_path(city_map, start, destination, route, travel_time)

        print("\n" + "="*80)
        print("ROUTE RECOMMENDATION")
        print("="*80)
        print(f"Recommended route: {' -> '.join(route)}")
        print(f"Total travel time: {travel_time} minutes")
        print(f"Number of stops: {len(route) - 1}")

        # Find alternative paths
        print("\n>>> Finding alternative routes...")
        all_routes = GraphTraversal.find_all_paths(city_map, start, destination, max_paths=3, verbose=False)

        if len(all_routes) > 1:
            print("\nAlternative Routes:")
            for i, alt_route in enumerate(all_routes[1:], 2):
                # Calculate distance for alternative route
                alt_distance = 0
                for j in range(len(alt_route) - 1):
                    alt_distance += city_map.get_edge_weight(alt_route[j], alt_route[j+1])
                print(f"  Route {i}: {' -> '.join(alt_route)}")
                print(f"           Travel time: {alt_distance} minutes")

        print("="*80)


def main():
    """Main function to run all demonstrations."""
    print("\n" + "#"*80)
    print("#" + " "*78 + "#")
    print("#" + "COMPREHENSIVE GRAPH SYSTEM DEMONSTRATION".center(78) + "#")
    print("#" + " "*78 + "#")
    print("#"*80)
    print("\nThis program demonstrates:")
    print("  1. Graph construction with adjacency matrix and adjacency list")
    print("  2. Basic graph operations (add/remove vertices and edges)")
    print("  3. Graph traversal algorithms (DFS and BFS)")
    print("  4. Shortest path algorithms (Dijkstra, Bellman-Ford, BFS)")
    print("  5. Performance analysis and comparison")
    print("  6. Visual representations and real-world applications")
    print("\n" + "#"*80)

    # Run all demonstrations
    demos = [
        ("Basic Operations", demo_basic_operations),
        ("Directed Graphs", demo_directed_graph),
        ("Traversal Algorithms", demo_traversal_algorithms),
        ("Shortest Path Algorithms", demo_shortest_path_algorithms),
        ("Advanced Scenarios", demo_advanced_scenarios),
        ("Performance Comparison", demo_performance_comparison),
        ("Real-World Application", demo_real_world_application)
    ]

    for i, (name, demo_func) in enumerate(demos, 1):
        try:
            demo_func()
            print(f"\n[OK] Demo {i} completed successfully\n")
        except Exception as e:
            print(f"\n[ERROR] Error in Demo {i}: {e}\n")

    # Final summary
    print("\n" + "#"*80)
    print("#" + " "*78 + "#")
    print("#" + "ALL DEMONSTRATIONS COMPLETED".center(78) + "#")
    print("#" + " "*78 + "#")
    print("#"*80)
    print("\nKey Takeaways:")
    print("  • Adjacency Matrix: Best for dense graphs, O(1) edge lookup")
    print("  • Adjacency List: Best for sparse graphs, memory efficient")
    print("  • DFS: Explores deeply, good for path finding and cycle detection")
    print("  • BFS: Explores by level, finds shortest path in unweighted graphs")
    print("  • Dijkstra: Finds shortest path in weighted graphs (no negative weights)")
    print("  • Bellman-Ford: Handles negative weights, detects negative cycles")
    print("\n" + "#"*80 + "\n")


if __name__ == "__main__":
    main()

