class Solution:
    def findSubsequences(self, nums: list[int]) -> list[list[int]]:
        """Backtracking with implicit deduplication for non-decreasing subsequences.

        Intuition:
            Generate all subsequences of length >= 2 that are non-decreasing.
            Avoid duplicates by not skipping an element if it equals the
            last chosen value (preventing identical branches).

        Approach:
            Use DFS with the current index, last chosen value, and current
            subsequence. At each position, include the element if it's >=
            last, then recurse. Skip the element only if it differs from
            last (preventing duplicate subsequences).

        Complexity:
            Time: O(2^n * n) — enumerate all valid subsequences
            Space: O(n) recursion depth plus O(2^n) for results
        """

        def dfs(index: int, last_value: int, current: list[int]) -> None:
            if index == len(nums):
                if len(current) > 1:
                    result.append(current[:])
                return
            if nums[index] >= last_value:
                current.append(nums[index])
                dfs(index + 1, nums[index], current)
                current.pop()
            if nums[index] != last_value:
                dfs(index + 1, last_value, current)

        result: list[list[int]] = []
        dfs(0, -1000, [])
        return result
