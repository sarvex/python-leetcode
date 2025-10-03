from typing import List

class Solution:
    def longestPath(self, parent: "List[int]", s: str) -> int:
        """Greedy DP from leaves using reverse topological processing

        Intuition:
        - The longest valid path either passes through an edge (u, v) with s[u] != s[v], combining the best arms from both sides, or is a single chain.

        Approach:
        - Compute each node's out-degree (number of children) from the parent array.
        - Initialize every node's best downward chain length as 1 (the node itself).
        - Start from leaves (out-degree 0) and push upward:
          - When processing a node i, try to extend its parent p if s[i] != s[p].
          - Maintain global best as height[p] + height[i] when characters differ.
          - Decrease parent's out-degree and push parent when it becomes 0.
        - This processes each edge once: O(n).

        Complexity:
        - Time: O(n)
        - Space: O(n)
        """

        n: int = len(s)
        if n <= 1:
            return n

        height: List[int] = [1] * n  # best downward chain length starting at node
        child_count: List[int] = [0] * n

        for p in parent[1:]:  # skip root's parent (-1)
            if p != -1:
                child_count[p] += 1

        nodes: List[int] = [i for i in range(n) if child_count[i] == 0]
        best: int = 1

        while nodes:
            i = nodes.pop()
            p = parent[i]

            if p != -1:
                if s[i] != s[p]:
                    hp, hi = height[p], height[i]
                    if hp + hi > best:
                        best = hp + hi
                    if hi + 1 > hp:
                        height[p] = hi + 1

                child_count[p] -= 1
                if child_count[p] == 0:
                    nodes.append(p)

        return best
