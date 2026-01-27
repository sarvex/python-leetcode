class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        """Backtracking with Duplicate Skipping

        Intuition:
            Sort the array so duplicates are adjacent, then use backtracking.
            After excluding a number, skip all its duplicates to avoid
            generating duplicate subsets.

        Approach:
            Sort nums. Use DFS: at each index, either include the current
            element and recurse, or exclude it and skip past all identical
            elements before recursing. Collect the subset when the index
            reaches the end.

        Complexity:
            Time: O(n * 2^n)
            Space: O(n) for recursion stack
        """

        def dfs(index: int) -> None:
            if index == len(nums):
                result.append(current[:])
                return
            current.append(nums[index])
            dfs(index + 1)
            skipped = current.pop()
            while index + 1 < len(nums) and nums[index + 1] == skipped:
                index += 1
            dfs(index + 1)

        nums.sort()
        result: list[list[int]] = []
        current: list[int] = []
        dfs(0)
        return result
