from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """Greedy approach to determine if you can reach the last index.

        Intuition:
        Track the maximum reachable position. If at any point we can't reach
        the current position, we fail. Otherwise, if we can process all elements,
        we can reach the end.

        Approach:
        Use a greedy algorithm that keeps track of the maximum index we can reach.
        For each position, check if we can reach it. If not, return False.
        Otherwise, update the maximum reachable position and continue.

        Complexity:
        Time: O(n) where n is the length of nums
        Space: O(1) as we only use constant extra space
        """
        max_reach = 0

        for i, jump_length in enumerate(nums):
            # If current position is beyond our reach, we can't proceed
            if max_reach < i:
                return False

            # Update the furthest position we can reach
            max_reach = max(max_reach, i + jump_length)

            # Early termination if we can already reach the end
            if max_reach >= len(nums) - 1:
                return True

        return True
