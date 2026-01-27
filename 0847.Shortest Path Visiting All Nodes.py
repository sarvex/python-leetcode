from collections import deque


class Solution:
    def shortestPathLength(self, graph: list[list[int]]) -> int:
        """BFS with bitmask state to find shortest path visiting all nodes.

        Intuition:
            Use BFS where each state is (current_node, visited_bitmask).
            Start from every node simultaneously and find the first state
            where all nodes are visited.

        Approach:
            1. Initialize BFS from each node with its bitmask set.
            2. Track visited (node, bitmask) states to avoid revisits.
            3. For each state, expand to neighbors updating the bitmask.
            4. Return the BFS level when the full bitmask is reached.

        Complexity:
            Time: O(2^n * n)
            Space: O(2^n * n)
        """
        num_nodes = len(graph)
        queue: deque[tuple[int, int]] = deque()
        visited: set[tuple[int, int]] = set()
        for node in range(num_nodes):
            queue.append((node, 1 << node))
            visited.add((node, 1 << node))
        full_mask = (1 << num_nodes) - 1
        steps = 0
        while True:
            for _ in range(len(queue)):
                current, mask = queue.popleft()
                if mask == full_mask:
                    return steps
                for neighbor in graph[current]:
                    new_mask = mask | (1 << neighbor)
                    if (neighbor, new_mask) not in visited:
                        visited.add((neighbor, new_mask))
                        queue.append((neighbor, new_mask))
            steps += 1
