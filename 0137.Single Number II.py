class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        """Bitwise Counting Approach

        Intuition:
            Every element appears three times except one. By counting bits at each
            position modulo 3, the remaining bits form the single number.

        Approach:
            For each of the 32 bit positions, sum that bit across all numbers.
            If the count mod 3 is non-zero, the single number has a 1 at that
            position. Handle the sign bit (position 31) separately for negative
            numbers.

        Complexity:
            Time: O(32 * n) = O(n) where n is the length of nums
            Space: O(1)
        """
        result = 0
        for i in range(32):
            bit_count = sum(num >> i & 1 for num in nums)
            if bit_count % 3:
                if i == 31:
                    result -= 1 << i
                else:
                    result |= 1 << i
        return result
