class Solution:
    def prefixesDivBy5(self, nums: list[int]) -> list[bool]:
        """Binary Prefix Divisible By 5.

        Intuition:
            Track the running binary number modulo 5. At each step, shift left
            and add the new bit, then check divisibility.

        Approach:
            Iterate through the array, maintaining the current value mod 5.
            For each bit, compute (current << 1 | bit) % 5 and record whether
            the result is zero.

        Complexity:
            Time: O(n)
            Space: O(n) for the result list
        """
        result: list[bool] = []
        remainder = 0
        for bit in nums:
            remainder = (remainder << 1 | bit) % 5
            result.append(remainder == 0)
        return result
