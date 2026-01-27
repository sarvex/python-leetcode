class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        """Bit Clearing Approach

        Intuition:
            The bitwise AND of a range eliminates all bits that differ
            between left and right. Clearing the lowest set bit of right
            until right <= left finds the common prefix.

        Approach:
            1. While right is greater than left, clear the lowest set bit
               of right using right & (right - 1).
            2. When right <= left, the remaining bits are the common prefix.

        Complexity:
            Time: O(log n) where n is the value of right
            Space: O(1)
        """
        while left < right:
            right &= right - 1
        return right
