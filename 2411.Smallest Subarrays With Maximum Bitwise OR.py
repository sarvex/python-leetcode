from typing import List


class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        """
        Highly optimized approach using rightmost bit position tracking for maximum OR subarrays.

        Intuition:
        For each position, find the smallest subarray starting there with maximum possible OR.
        Track the rightmost position where each bit appears to determine required subarray length.

        Approach:
        Process array from right to left, maintaining rightmost positions of each bit.
        Track the maximum position directly to avoid expensive max() calls on all bit positions.

        Complexity:
        Time: O(n) - single pass with constant bit operations
        Space: O(1) - fixed array for 32 bit positions
        """
        n = len(nums)
        result = [1] * n
        bit_positions = [-1] * 32

        for i in range(n - 1, -1, -1):
            # Update positions for all set bits in current number
            # Track the furthest position directly
            furthest_pos = i
            for bit in range(32):
                if nums[i] & (1 << bit):
                    bit_positions[bit] = i
                # Update furthest position from existing bit positions
                if bit_positions[bit] > furthest_pos:
                    furthest_pos = bit_positions[bit]

            # The required subarray extends to the furthest bit position
            result[i] = furthest_pos - i + 1

        return result
