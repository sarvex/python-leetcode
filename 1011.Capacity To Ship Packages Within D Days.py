from bisect import bisect_left


class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        """Find the minimum ship capacity to ship all packages within given days.

        Intuition:
            The answer is monotonic: if capacity c works, any c' > c also works.
            Binary search on the capacity to find the minimum feasible value.

        Approach:
            Binary search between max(weights) and sum(weights). For each
            candidate capacity, greedily simulate shipping and count days needed.

        Complexity:
            Time: O(n * log(sum - max)) for binary search with linear check
            Space: O(1)
        """

        def can_ship(capacity: int) -> bool:
            current_weight, day_count = 0, 1
            for weight in weights:
                current_weight += weight
                if current_weight > capacity:
                    day_count += 1
                    current_weight = weight
            return day_count <= days

        left, right = max(weights), sum(weights) + 1
        return left + bisect_left(range(left, right), True, key=can_ship)
