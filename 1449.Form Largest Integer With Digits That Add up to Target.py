from math import inf


class Solution:
    def largestNumber(self, cost: list[int], target: int) -> str:
        """Form the largest integer whose digit costs sum to target.

        Intuition:
            Maximize the number of digits first (more digits = larger number),
            then greedily pick the largest digit at each position.

        Approach:
            Use complete knapsack DP where dp[i][j] stores the maximum number
            of digits achievable using digits 1..i with cost exactly j. Track
            choices in a backtracking table to reconstruct the answer by always
            preferring larger digits first.

        Complexity:
            Time: O(9 * target)
            Space: O(9 * target)
        """
        dp = [[-inf] * (target + 1) for _ in range(10)]
        dp[0][0] = 0
        backtrack = [[0] * (target + 1) for _ in range(10)]

        for digit, digit_cost in enumerate(cost, 1):
            for budget in range(target + 1):
                if (
                    budget < digit_cost
                    or dp[digit][budget - digit_cost] + 1 < dp[digit - 1][budget]
                ):
                    dp[digit][budget] = dp[digit - 1][budget]
                    backtrack[digit][budget] = budget
                else:
                    dp[digit][budget] = dp[digit][budget - digit_cost] + 1
                    backtrack[digit][budget] = budget - digit_cost

        if dp[9][target] < 0:
            return "0"

        result: list[str] = []
        digit, remaining = 9, target
        while digit:
            if remaining == backtrack[digit][remaining]:
                digit -= 1
            else:
                result.append(str(digit))
                remaining = backtrack[digit][remaining]
        return "".join(result)
