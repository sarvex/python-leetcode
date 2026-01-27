from collections import deque


class Solution:
    def findMinHeightTrees(self, n: int, edges: list[list[int]]) -> list[int]:
        """Topological peeling of leaf nodes to find tree centroids.

        Intuition:
            The roots of minimum height trees are the centroids of the tree,
            found by repeatedly removing leaf nodes layer by layer.

        Approach:
            1. Build an adjacency list and compute the degree of each node.
            2. Initialize a queue with all leaf nodes (degree 1).
            3. Repeatedly peel off the current leaf layer, reducing neighbor
               degrees and adding new leaves to the queue.
            4. The last layer of nodes remaining are the MHT roots.

        Complexity:
            Time: O(n) where n is the number of nodes
            Space: O(n) for the adjacency list and queue
        """
        if n == 1:
            return [0]
        adjacency = [[] for _ in range(n)]
        degree = [0] * n
        for node_a, node_b in edges:
            adjacency[node_a].append(node_b)
            adjacency[node_b].append(node_a)
            degree[node_a] += 1
            degree[node_b] += 1
        queue = deque(i for i in range(n) if degree[i] == 1)
        result = []
        while queue:
            result.clear()
            for _ in range(len(queue)):
                node = queue.popleft()
                result.append(node)
                for neighbor in adjacency[node]:
                    degree[neighbor] -= 1
                    if degree[neighbor] == 1:
                        queue.append(neighbor)
        return result
