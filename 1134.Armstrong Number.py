class Solution:
    def isArmstrong(self, n: int) -> bool:
        """Check if n is an Armstrong number.

        Intuition:
            An Armstrong number equals the sum of its digits each raised to
            the power of the total number of digits.

        Approach:
            Compute the digit count, then iterate through digits summing each
            raised to that power. Compare the sum to the original number.

        Complexity:
            Time: O(d) where d is the number of digits
            Space: O(1)
        """
        num_digits = len(str(n))
        digit_power_sum = 0
        remaining = n
        while remaining:
            digit_power_sum += (remaining % 10) ** num_digits
            remaining //= 10
        return digit_power_sum == n
