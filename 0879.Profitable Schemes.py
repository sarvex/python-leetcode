from functools import cache


class Solution:
    def profitableSchemes(
        self, n: int, minProfit: int, group: list[int], profit: list[int]
    ) -> int:
        """Memoized DFS exploring crime inclusion with member and profit constraints.

        Intuition:
            For each crime, decide to include it or not, tracking the number
            of members used and profit accumulated. Count schemes meeting
            the minimum profit threshold.

        Approach:
            1. Define a recursive function with crime index, members used,
               and current profit as state.
            2. At each crime, either skip it or include it (if enough members).
            3. Cap profit at minProfit to reduce state space.
            4. Base case: all crimes considered, count if profit meets threshold.

        Complexity:
            Time: O(len(group) * n * minProfit)
            Space: O(len(group) * n * minProfit)
        """
        modulo = 10**9 + 7

        @cache
        def search(crime_index: int, members_used: int, current_profit: int) -> int:
            if crime_index >= len(group):
                return 1 if current_profit == minProfit else 0
            count = search(crime_index + 1, members_used, current_profit)
            if members_used + group[crime_index] <= n:
                count += search(
                    crime_index + 1,
                    members_used + group[crime_index],
                    min(current_profit + profit[crime_index], minProfit),
                )
            return count % modulo

        return search(0, 0, 0)
