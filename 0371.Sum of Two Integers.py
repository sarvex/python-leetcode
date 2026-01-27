class Solution:
    def getSum(self, a: int, b: int) -> int:
        """Sum two integers without using + or - via bitwise operations.

        Intuition:
            XOR gives the sum without carries, and AND shifted left gives the
            carries. Repeat until there are no more carries.

        Approach:
            Mask both numbers to 32-bit unsigned integers. In each iteration,
            compute the carry as (a AND b) shifted left by 1, and the partial
            sum as a XOR b. Repeat until carry is zero. Convert back to signed
            32-bit integer if the result exceeds the positive range.

        Complexity:
            Time: O(1) - at most 32 iterations
            Space: O(1)
        """
        a, b = a & 0xFFFFFFFF, b & 0xFFFFFFFF
        while b:
            carry = ((a & b) << 1) & 0xFFFFFFFF
            a, b = a ^ b, carry
        return a if a < 0x80000000 else ~(a ^ 0xFFFFFFFF)
