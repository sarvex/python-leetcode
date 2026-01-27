from collections import defaultdict


class Node:
    def __init__(self, val: int = 0, neighbors: list["Node"] | None = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Node | None) -> Node | None:
        """DFS with Hash Map Cloning Approach

        Intuition:
            To clone a graph, we need to create a copy of each node and replicate
            all edges. A hash map tracks already-cloned nodes to handle cycles and
            avoid duplicates.

        Approach:
            Use DFS with a visited dictionary mapping original nodes to clones.
            For each unvisited node, create a clone, store it, then recursively
            clone all neighbors and append them to the clone's neighbor list.

        Complexity:
            Time: O(n + e) where n is nodes and e is edges
            Space: O(n) for the visited map and recursion stack
        """
        visited: dict[Node, Node] = defaultdict()

        def clone(original: Node | None) -> Node | None:
            if original is None:
                return None
            if original in visited:
                return visited[original]
            copy = Node(original.val)
            visited[original] = copy
            for neighbor in original.neighbors:
                copy.neighbors.append(clone(neighbor))
            return copy

        return clone(node)
