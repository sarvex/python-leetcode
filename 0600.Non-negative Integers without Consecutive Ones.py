from functools import cache


class Solution:
    def findIntegers(self, n: int) -> int:
        """Count non-negative integers up to n without consecutive ones in binary.

        Intuition:
            Use digit DP on the binary representation. At each bit position,
            decide whether to place 0 or 1, ensuring no two consecutive 1s.

        Approach:
            1. Extract the binary digits of n into an array.
            2. Use memoized DFS with state (position, previous_bit, is_tight).
            3. At each position, try placing 0 or 1, skip if previous was 1 and
               current is 1 (consecutive ones).
            4. The tight constraint limits choices to the actual digit when active.

        Complexity:
            Time: O(log n)
            Space: O(log n)
        """

        @cache
        def search(pos: int, previous: int, is_tight: bool) -> int:
            if pos <= 0:
                return 1
            upper = bits[pos] if is_tight else 1
            count = 0
            for digit in range(upper + 1):
                if previous == 1 and digit == 1:
                    continue
                count += search(pos - 1, digit, is_tight and digit == upper)
            return count

        bits = [0] * 33
        bit_length = 0
        while n:
            bit_length += 1
            bits[bit_length] = n & 1
            n >>= 1
        return search(bit_length, 0, True)
