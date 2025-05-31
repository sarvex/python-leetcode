from typing import List

class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]]) -> List[int]:
        """Bipartite graph coloring to maximize target nodes after connecting trees

        Intuition: The problem can be solved using bipartite coloring of both trees and
        finding the optimal connection point to maximize target nodes.

        Approach:
        1. Build adjacency lists for both trees
        2. Color both trees using bipartite coloring (nodes at even/odd distances)
        3. Count nodes of each color in both trees
        4. For each node in tree1, calculate maximum target nodes by connecting it to tree2

        Complexity:
        Time: O(n + m) where n and m are the number of nodes in the two trees
        Space: O(n + m) for storing the adjacency lists and coloring information
        """
        def build_adjacency_list(edges: List[List[int]]) -> List[List[int]]:
            """Build an adjacency list representation of a tree from edge list"""
            n = len(edges) + 1
            graph = [[] for _ in range(n)]
            for u, v in edges:
                graph[u].append(v)
                graph[v].append(u)
            return graph

        def color_tree(graph: List[List[int]], node: int, parent: int, colors: List[int],
                      color: int, color_counts: List[int]) -> None:
            """Color the tree using bipartite coloring and count nodes of each color"""
            colors[node] = color
            color_counts[color] += 1

            for neighbor in graph[node]:
                if neighbor != parent:
                    # Alternate colors (0/1) using XOR
                    color_tree(graph, neighbor, node, colors, color ^ 1, color_counts)

        # Build adjacency lists for both trees
        graph1 = build_adjacency_list(edges1)
        graph2 = build_adjacency_list(edges2)

        # Get sizes of both trees
        n, m = len(graph1), len(graph2)

        # Initialize coloring arrays and counters
        colors1 = [0] * n
        colors2 = [0] * m
        color_counts1 = [0, 0]  # Count of nodes with color 0 and 1 in tree1
        color_counts2 = [0, 0]  # Count of nodes with color 0 and 1 in tree2

        # Color both trees starting from node 0
        color_tree(graph2, 0, -1, colors2, 0, color_counts2)
        color_tree(graph1, 0, -1, colors1, 0, color_counts1)

        # Find the maximum count of nodes of either color in tree2
        max_color_count = max(color_counts2)

        # For each node in tree1, calculate the maximum target nodes
        # by adding the count of nodes with the same color in tree1
        return [max_color_count + color_counts1[colors1[i]] for i in range(n)]
