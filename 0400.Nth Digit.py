class Solution:
    def findNthDigit(self, n: int) -> int:
        """Find the nth digit in the infinite integer sequence.

        Intuition:
            Digits are grouped by number length: 1-digit numbers contribute
            9*1 digits, 2-digit numbers contribute 90*2 digits, etc. We can
            skip entire groups to locate which number contains the nth digit.

        Approach:
            1. Determine the digit-length group by subtracting group sizes.
            2. Compute the actual number within that group.
            3. Find the specific digit within that number.

        Complexity:
            Time: O(log n)
            Space: O(1)
        """
        digit_length, group_count = 1, 9
        while digit_length * group_count < n:
            n -= digit_length * group_count
            digit_length += 1
            group_count *= 10
        target_number = 10 ** (digit_length - 1) + (n - 1) // digit_length
        digit_index = (n - 1) % digit_length
        return int(str(target_number)[digit_index])
