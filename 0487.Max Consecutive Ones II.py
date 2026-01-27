class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        """Sliding window allowing at most one zero flip.

        Intuition:
            Use a sliding window that tolerates at most one zero. When
            the zero count exceeds one, shrink from the left.

        Approach:
            Expand the window rightward. Count zeros by XOR with 1. If
            the zero count exceeds 1, shrink from the left, adjusting
            the count. The result is the total length minus the left
            pointer.

        Complexity:
            Time: O(n)
            Space: O(1)
        """
        left = zero_count = 0
        for value in nums:
            zero_count += value ^ 1
            if zero_count > 1:
                zero_count -= nums[left] ^ 1
                left += 1
        return len(nums) - left
