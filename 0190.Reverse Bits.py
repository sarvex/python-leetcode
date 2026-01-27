class Solution:
    def reverseBits(self, n: int) -> int:
        """Bit Manipulation Approach

        Intuition:
            Extract each bit from the least significant end and place it
            at the corresponding position from the most significant end.

        Approach:
            1. Iterate through all 32 bits of the integer.
            2. Extract the least significant bit using AND with 1.
            3. Place it at position (31 - i) in the result using left shift.
            4. Right shift n to process the next bit.

        Complexity:
            Time: O(1) - always processes exactly 32 bits
            Space: O(1)
        """
        result = 0
        for i in range(32):
            result |= (n & 1) << (31 - i)
            n >>= 1
        return result
