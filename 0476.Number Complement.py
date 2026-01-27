class Solution:
    def findComplement(self, num: int) -> int:
        """XOR with all-ones mask of the same bit length.

        Intuition:
            The complement flips all bits. XOR with a mask of all 1s of
            the same bit length achieves this.

        Approach:
            Compute a mask with all bits set up to the highest bit of num,
            then XOR num with that mask.

        Complexity:
            Time: O(1)
            Space: O(1)
        """
        return num ^ ((1 << num.bit_length()) - 1)
