from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        Backtracking approach to generate all possible subsets

        Intuition:
        For each element in the array, we have two choices: either include it in the
        current subset or exclude it. We can use recursion to explore all possibilities.

        Approach:
        Use depth-first search (DFS) with backtracking to generate all subsets.
        For each position, we make two recursive calls:
        1. Skip the current element (exclude it)
        2. Include the current element, then backtrack by removing it after recursion

        Complexity:
        Time: O(2^n) where n is the length of nums (2^n possible subsets)
        Space: O(n) for recursion stack and temporary subset storage
        """
        def dfs(i: int) -> None:
            # Base case: when we've processed all elements
            if i == len(nums):
                ans.append(t[:])
                return

            # Decision 1: Skip current element
            dfs(i + 1)

            # Decision 2: Include current element
            t.append(nums[i])
            dfs(i + 1)

            # Backtrack: remove the element we added
            t.pop()

        ans: List[List[int]] = []
        t: List[int] = []
        dfs(0)
        return ans
