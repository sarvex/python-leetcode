class Solution:
    def sumSubseqWidths(self, nums: list[int]) -> int:
        """Sorted array with power-of-two contribution counting.

        Intuition:
            After sorting, each element contributes as the max of some
            subsequences and the min of others. The net contribution of
            nums[i] is nums[i] * (2^i - 2^(n-1-i)).

        Approach:
            1. Sort the array.
            2. Iterate with a doubling power multiplier.
            3. For each index i, add (nums[i] - nums[n-1-i]) * 2^i to the result.

        Complexity:
            Time: O(n log n)
            Space: O(1) excluding sort space
        """
        modulo = 10**9 + 7
        nums.sort()
        total = 0
        power = 1
        for index, value in enumerate(nums):
            total = (total + (value - nums[-index - 1]) * power) % modulo
            power = (power << 1) % modulo
        return total
