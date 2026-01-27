class Solution:
    def numberOfPatterns(self, m: int, n: int) -> int:
        """Backtracking with symmetry optimization for unlock patterns.

        Intuition:
            Use DFS to explore all valid patterns of length m to n. Exploit
            symmetry: patterns starting from corners (1,3,7,9) are equivalent,
            as are those from edges (2,4,6,8).

        Approach:
            1. Precompute the crossing table: cross[i][j] is the key that
               must be visited before going from i to j.
            2. DFS from each starting key, counting patterns of valid length.
            3. Multiply corner result by 4, edge result by 4, and add center.

        Complexity:
            Time: O(n!) in the worst case, bounded by pattern count
            Space: O(n) for the recursion stack and visited array
        """

        def dfs(key: int, length: int = 1) -> int:
            if length > n:
                return 0
            visited[key] = True
            count = int(length >= m)
            for next_key in range(1, 10):
                crossing = cross[key][next_key]
                if not visited[next_key] and (crossing == 0 or visited[crossing]):
                    count += dfs(next_key, length + 1)
            visited[key] = False
            return count

        cross = [[0] * 10 for _ in range(10)]
        cross[1][3] = cross[3][1] = 2
        cross[1][7] = cross[7][1] = 4
        cross[1][9] = cross[9][1] = 5
        cross[2][8] = cross[8][2] = 5
        cross[3][7] = cross[7][3] = 5
        cross[3][9] = cross[9][3] = 6
        cross[4][6] = cross[6][4] = 5
        cross[7][9] = cross[9][7] = 8
        visited = [False] * 10
        return dfs(1) * 4 + dfs(2) * 4 + dfs(5)
