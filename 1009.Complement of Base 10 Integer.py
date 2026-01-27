class Solution:
    def bitwiseComplement(self, n: int) -> int:
        """Return the complement of a base-10 integer in binary.

        Intuition:
            Flip each bit in the binary representation. The complement equals
            the XOR with a mask of all 1s of the same bit length.

        Approach:
            Scan from the most significant bit downward. Once a set bit is found,
            flip all subsequent bits by setting unset bits in the result.

        Complexity:
            Time: O(log n) for scanning up to 31 bits
            Space: O(1)
        """
        if n == 0:
            return 1
        result = 0
        found_msb = False
        for bit_pos in range(30, -1, -1):
            bit_value = n & (1 << bit_pos)
            if not found_msb and bit_value == 0:
                continue
            found_msb = True
            if bit_value == 0:
                result |= 1 << bit_pos
        return result
