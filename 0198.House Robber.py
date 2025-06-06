from typing import List
from functools import cache


class Solution:
    def rob(self, nums: List[int]) -> int:
        """Dynamic Programming: Bottom-up tabulation with space optimization

        Intuition:
        At each house, we have two options: rob it or skip it. If we rob the current house,
        we can't rob the adjacent one. The goal is to maximize the total amount robbed.

        Approach:
        Use dynamic programming with space optimization. We only need to keep track of the
        maximum money we can rob up to the previous house and the house before that.

        Complexity:
        - Time: O(n) where n is the number of houses
        - Space: O(1) constant extra space
        """
        n = len(nums)

        # Handle edge cases
        if not nums:
            return 0
        if n == 1:
            return nums[0]

        # Initialize variables to track maximum money robbed
        rob1, rob2 = 0, 0  # rob1: two houses ago, rob2: previous house

        # Iterate through all houses
        for num in nums:
            # Choose maximum between robbing current house or skipping it
            rob1, rob2 = rob2, max(rob1 + num, rob2)

        return rob2

    def rob_recursive(self, nums: List[int]) -> int:
        """Dynamic Programming: Top-down memoization approach

        Intuition:
        For each house, decide whether to rob it (and skip the next) or skip it.

        Approach:
        Use recursive approach with memoization to avoid redundant calculations.

        Complexity:
        - Time: O(n) where n is the number of houses
        - Space: O(n) for the recursion stack and memoization cache
        """
        @cache
        def dfs(i: int) -> int:
            if i >= len(nums):
                return 0
            return max(nums[i] + dfs(i + 2), dfs(i + 1))  # Rob current or skip

        return dfs(0)
