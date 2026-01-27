from math import inf


class Solution:
    def maxVacationDays(self, flights: list[list[int]], days: list[list[int]]) -> int:
        """Maximize vacation days across weeks using DP with flight transitions.

        Intuition:
            At each week, we can stay in the current city or fly to another.
            We use DP where dp[k][j] represents the max vacation days after
            week k ending in city j.

        Approach:
            1. Initialize dp[0][0] = 0, all others to -infinity.
            2. For each week k, for each city j, check all cities i with a
               flight to j (or staying in j).
            3. Add the vacation days for city j in week k.
            4. Return the maximum over all cities in the last week.

        Complexity:
            Time: O(K * n^2) where K is number of weeks and n is number of cities
            Space: O(K * n)
        """
        num_cities = len(flights)
        num_weeks = len(days[0])
        dp = [[-inf] * num_cities for _ in range(num_weeks + 1)]
        dp[0][0] = 0
        for week in range(1, num_weeks + 1):
            for destination in range(num_cities):
                dp[week][destination] = dp[week - 1][destination]
                for origin in range(num_cities):
                    if flights[origin][destination]:
                        dp[week][destination] = max(
                            dp[week][destination], dp[week - 1][origin]
                        )
                dp[week][destination] += days[destination][week - 1]
        return max(dp[-1][j] for j in range(num_cities))
