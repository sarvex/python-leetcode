from collections import deque


class Solution:
    def allPathsSourceTarget(self, graph: list[list[int]]) -> list[list[int]]:
        """BFS to enumerate all paths from source to target in a DAG.

        Intuition:
            Since the graph is a DAG, every path from node 0 to node n-1 is
            finite. We can use BFS to explore all possible paths.

        Approach:
            1. Initialize a queue with the path [0].
            2. For each path, extend it by appending each neighbor of the last node.
            3. If the last node is n-1, add the path to results.

        Complexity:
            Time: O(2^n * n) in the worst case for all possible paths
            Space: O(2^n * n) to store all paths
        """
        target = len(graph) - 1
        queue: deque[list[int]] = deque([[0]])
        result: list[list[int]] = []
        while queue:
            path = queue.popleft()
            current = path[-1]
            if current == target:
                result.append(path)
                continue
            for neighbor in graph[current]:
                queue.append(path + [neighbor])
        return result
