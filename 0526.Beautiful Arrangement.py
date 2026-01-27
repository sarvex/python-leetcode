from collections import defaultdict


class Solution:
    def countArrangement(self, n: int) -> int:
        """Backtracking with precomputed divisibility matches.

        Intuition:
            For each position, only certain values are valid (divisibility
            condition). Precompute valid matches and use backtracking to count
            all valid permutations.

        Approach:
            Build a mapping of valid values for each position based on
            divisibility. Use DFS with a visited array to enumerate all
            beautiful arrangements.

        Complexity:
            Time: O(k) where k is number of valid permutations
            Space: O(n)
        """

        def dfs(position: int) -> None:
            nonlocal count, n
            if position == n + 1:
                count += 1
                return
            for value in valid_matches[position]:
                if not visited[value]:
                    visited[value] = True
                    dfs(position + 1)
                    visited[value] = False

        count = 0
        visited = [False] * (n + 1)
        valid_matches: dict[int, list[int]] = defaultdict(list)
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if j % i == 0 or i % j == 0:
                    valid_matches[i].append(j)

        dfs(1)
        return count
