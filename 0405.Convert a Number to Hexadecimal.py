class Solution:
    def toHex(self, num: int) -> str:
        """Convert integer to hexadecimal using bit extraction.

        Intuition:
            Extract 4 bits at a time from the 32-bit representation,
            starting from the most significant nibble, skipping leading zeros.

        Approach:
            1. Handle special case of 0 directly.
            2. Iterate from the highest nibble (position 7) to lowest (position 0).
            3. Extract each 4-bit group using right-shift and mask with 0xF.
            4. Skip leading zeros, then append hex characters.

        Complexity:
            Time: O(1) since we always process exactly 8 nibbles
            Space: O(1)
        """
        if num == 0:
            return "0"
        hex_chars = "0123456789abcdef"
        result: list[str] = []
        for i in range(7, -1, -1):
            nibble = (num >> (4 * i)) & 0xF
            if result or nibble != 0:
                result.append(hex_chars[nibble])
        return "".join(result)
