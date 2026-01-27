from collections import deque


class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: list[str]) -> int:
        """BFS to find shortest mutation path differing by one character at each step.

        Intuition:
            Each valid mutation changes exactly one character and must be in the
            gene bank. BFS finds the shortest path in an unweighted graph.

        Approach:
            1. Initialize BFS queue with the start gene and depth 0.
            2. For each gene, check all bank genes differing by exactly one char.
            3. If end gene is reached, return the depth.
            4. Mark visited genes to avoid cycles. Return -1 if unreachable.

        Complexity:
            Time: O(n * L) where n is the bank size and L is gene length (8).
            Space: O(n) for the visited set and queue.
        """
        queue = deque([(startGene, 0)])
        visited = {startGene}
        while queue:
            gene, depth = queue.popleft()
            if gene == endGene:
                return depth
            for next_gene in bank:
                differences = sum(a != b for a, b in zip(gene, next_gene))
                if differences == 1 and next_gene not in visited:
                    queue.append((next_gene, depth + 1))
                    visited.add(next_gene)
        return -1
