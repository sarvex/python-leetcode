class Solution:
    def sumOfDigits(self, nums: list[int]) -> int:
        """Return 1 if digit sum of minimum is even, 0 if odd.

        Intuition:
            Find the minimum, compute its digit sum, and check parity.

        Approach:
            Extract minimum value, sum its digits by repeated mod/div,
            then XOR the parity bit with 1 to invert.

        Complexity:
            Time: O(n + log(min_val))
            Space: O(1)
        """
        min_val = min(nums)
        digit_sum = 0
        while min_val:
            digit_sum += min_val % 10
            min_val //= 10
        return digit_sum & 1 ^ 1
