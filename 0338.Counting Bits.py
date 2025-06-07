from typing import List

class Solution:
    def countBits(self, n: int) -> List[int]:
        """Count the number of 1's in binary representation of each number from 0 to n.

        Intuition:
            We can use Python's built-in bit_count method to count the number of 1's
            in the binary representation of each integer.

        Approach:
            Use a list comprehension to iterate from 0 to n and apply bit_count to each number.
            Python's bit_count method efficiently counts the number of 1's in the binary
            representation of an integer.

        Complexity:
            Time: O(n) - We process each number from 0 to n once
            Space: O(n) - We store the result for each number from 0 to n
        """
        return [i.bit_count() for i in range(n + 1)]

    def countBits_dp(self, n: int) -> List[int]:
        """Count the number of 1's in binary representation using dynamic programming.

        Intuition:
            The number of 1's in i can be calculated from the number of 1's in i//2
            plus whether the least significant bit is set.

        Approach:
            Use dynamic programming where dp[i] = dp[i >> 1] + (i & 1)
            This works because shifting i right by 1 gives us a number with the same
            bit pattern except for the least significant bit, which we check separately.

        Complexity:
            Time: O(n) - We process each number from 0 to n once
            Space: O(n) - We store the result for each number from 0 to n
        """
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            dp[i] = dp[i >> 1] + (i & 1)
        return dp
