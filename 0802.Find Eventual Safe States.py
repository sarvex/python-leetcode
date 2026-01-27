from collections import defaultdict, deque


class Solution:
    def eventualSafeNodes(self, graph: list[list[int]]) -> list[int]:
        """Topological sort on reversed graph to find safe nodes.

        Intuition:
            Terminal nodes (no outgoing edges) are safe. Nodes that only lead
            to safe nodes are also safe. Reverse the graph and do topological
            sort starting from terminal nodes.

        Approach:
            1. Build a reverse graph and track out-degrees.
            2. Initialize a queue with all terminal nodes (out-degree 0).
            3. Process nodes via BFS, decrementing in-degrees of predecessors.
            4. All nodes with final out-degree 0 are safe.

        Complexity:
            Time: O(V + E)
            Space: O(V + E)
        """
        reverse_graph: defaultdict[int, list[int]] = defaultdict(list)
        out_degree = [0] * len(graph)
        for node, neighbors in enumerate(graph):
            for neighbor in neighbors:
                reverse_graph[neighbor].append(node)
            out_degree[node] = len(neighbors)
        queue = deque(i for i, degree in enumerate(out_degree) if degree == 0)
        while queue:
            node = queue.popleft()
            for predecessor in reverse_graph[node]:
                out_degree[predecessor] -= 1
                if out_degree[predecessor] == 0:
                    queue.append(predecessor)
        return [i for i, degree in enumerate(out_degree) if degree == 0]
