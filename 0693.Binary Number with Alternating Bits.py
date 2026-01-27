class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        """Bit-by-bit check for alternating 0s and 1s.

        Intuition:
            Compare each bit with the previous one. If any two consecutive
            bits are the same, the number does not have alternating bits.

        Approach:
            1. Track the previous bit value.
            2. Extract the lowest bit, compare with previous.
            3. If they match, return False. Otherwise continue shifting.

        Complexity:
            Time: O(log n) for the number of bits
            Space: O(1) constant extra space
        """
        previous_bit = -1
        while n:
            current_bit = n & 1
            if previous_bit == current_bit:
                return False
            previous_bit = current_bit
            n >>= 1
        return True
