class Solution:
    def isOneBitCharacter(self, bits: list[int]) -> bool:
        """Greedy scan to check if last character is one-bit.

        Intuition:
            A 1-bit character is just [0], while 2-bit characters start with 1.
            Greedily consume characters from left to right and check if the
            last consumed character starts at the final position.

        Approach:
            1. Start from index 0 and advance by 1 + bits[i] each step.
            2. If bits[i] is 0, advance by 1; if bits[i] is 1, advance by 2.
            3. After the loop, check if we landed exactly on the last index.

        Complexity:
            Time: O(n) where n is the length of bits
            Space: O(1)
        """
        index, length = 0, len(bits)
        while index < length - 1:
            index += bits[index] + 1
        return index == length - 1
