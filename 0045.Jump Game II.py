from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        """Greedy approach to find minimum jumps to reach the end of array.

        Intuition:
        At each position, we want to maximize how far we can reach. When we
        reach the furthest position from our previous jump, we must make
        another jump to continue moving forward.

        Approach:
        1. Track current maximum reach and the furthest position we've reached
           in the current jump
        2. For each position (except the last), update maximum reach
        3. When we reach the furthest position from our previous jump,
           increment jump count and update furthest position

        Complexity:
        Time: O(n) where n is the length of nums, we process each element once
        Space: O(1) using only constant extra space
        """
        jumps = 0
        max_reach = 0
        furthest = 0

        # No need to consider the last element as we're already at destination
        for i, jump_distance in enumerate(nums[:-1]):
            # Update the furthest position we can reach from current position
            max_reach = max(max_reach, i + jump_distance)

            # If we've reached the furthest position from our previous jump
            if furthest == i:
                # We must make another jump
                jumps += 1
                # Update the furthest we can go with this new jump
                furthest = max_reach

        return jumps
