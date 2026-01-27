class Solution:
    def hammingWeight(self, n: int) -> int:
        """Brian Kernighan's Algorithm

        Intuition:
            Each n & (n - 1) operation clears the lowest set bit,
            so counting iterations gives the number of 1 bits.

        Approach:
            1. While n is non-zero, clear the lowest set bit with n & (n - 1).
            2. Increment the count for each cleared bit.
            3. Return the total count.

        Complexity:
            Time: O(k) where k is the number of set bits
            Space: O(1)
        """
        count = 0
        while n:
            n &= n - 1
            count += 1
        return count
