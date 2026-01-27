class Solution:
    def encode(self, num: int) -> str:
        """Encode a number as a binary string by mapping to (num+1) without leading bit.

        Intuition:
            The encoding pattern corresponds to the binary representation of
            (num + 1) with the leading '1' bit removed. This creates a bijective
            mapping from non-negative integers to binary strings.

        Approach:
            Compute num + 1, convert to binary, and strip the leading '1' bit
            by slicing from index 3 (skipping '0b1' prefix).

        Complexity:
            Time: O(log n) — binary conversion
            Space: O(log n) — for the binary string
        """
        return bin(num + 1)[3:]
