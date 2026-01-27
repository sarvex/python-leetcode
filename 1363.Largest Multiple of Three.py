from math import inf


class Solution:
    def largestMultipleOfThree(self, digits: list[int]) -> str:
        """Find the largest multiple of three from given digits.

        Intuition:
            A number is divisible by three if the sum of its digits is
            divisible by three. Use dynamic programming to select the maximum
            count of digits whose sum has remainder zero modulo three.

        Approach:
            Sort digits ascending. Use DP where f[i][j] tracks the maximum
            number of digits from the first i digits with digit-sum remainder
            j mod 3. Backtrack to reconstruct the chosen digits, then strip
            leading zeros.

        Complexity:
            Time: O(n) where n is the number of digits.
            Space: O(n)
        """
        digits.sort()
        n = len(digits)
        dp = [[-inf] * 3 for _ in range(n + 1)]
        dp[0][0] = 0

        for i, digit in enumerate(digits, 1):
            for remainder in range(3):
                dp[i][remainder] = max(
                    dp[i - 1][remainder],
                    dp[i - 1][(remainder - digit % 3 + 3) % 3] + 1,
                )

        if dp[n][0] <= 0:
            return ""

        selected: list[int] = []
        remainder = 0
        for i in range(n, 0, -1):
            prev_remainder = (remainder - digits[i - 1] % 3 + 3) % 3
            if dp[i - 1][prev_remainder] + 1 == dp[i][remainder]:
                selected.append(digits[i - 1])
                remainder = prev_remainder

        start = 0
        while start < len(selected) - 1 and selected[start] == 0:
            start += 1

        return "".join(map(str, selected[start:]))
