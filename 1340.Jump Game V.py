from functools import cache


class Solution:
    def maxJumps(self, arr: list[int], d: int) -> int:
        """Find the maximum number of indices you can visit by jumping.

        Intuition:
            From each index, you can jump left or right up to d positions as
            long as all intermediate values are strictly less. Use memoized DFS.

        Approach:
            For each index, DFS explores valid jumps in both directions,
            stopping when a value >= current is encountered or distance d
            is exceeded. Cache results for overlapping subproblems.

        Complexity:
            Time: O(n * d)
            Space: O(n)
        """
        length = len(arr)

        @cache
        def dfs(index: int) -> int:
            best = 1
            for j in range(index - 1, -1, -1):
                if index - j > d or arr[j] >= arr[index]:
                    break
                best = max(best, 1 + dfs(j))
            for j in range(index + 1, length):
                if j - index > d or arr[j] >= arr[index]:
                    break
                best = max(best, 1 + dfs(j))
            return best

        return max(dfs(i) for i in range(length))
