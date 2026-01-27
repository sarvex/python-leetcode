class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> list[int]:
        """Filter numbers divisible by each of their own digits.

        Intuition:
            A self-dividing number has no zero digits and is divisible by
            every digit it contains. Check each number in the range.

        Approach:
            1. Iterate through each number in [left, right].
            2. For each number, check every digit is non-zero and divides
               the number evenly.
            3. Collect all qualifying numbers.

        Complexity:
            Time: O((right - left) * d) where d is max digits per number
            Space: O(1) excluding output
        """
        return [
            num
            for num in range(left, right + 1)
            if all(digit != "0" and num % int(digit) == 0 for digit in str(num))
        ]
