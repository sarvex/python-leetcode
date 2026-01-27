class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        """Information theory: find minimum pigs using test rounds as a base.

        Intuition:
            Each pig can encode (rounds + 1) outcomes (die in round 1, 2, ..., or
            survive). With p pigs, we can distinguish (rounds+1)^p buckets.

        Approach:
            1. Compute the base as (minutesToTest // minutesToDie) + 1.
            2. Find the minimum number of pigs p such that base^p >= buckets.

        Complexity:
            Time: O(log(buckets) / log(base)) for the loop.
            Space: O(1) with no extra storage.
        """
        base = minutesToTest // minutesToDie + 1
        pig_count, capacity = 0, 1
        while capacity < buckets:
            capacity *= base
            pig_count += 1
        return pig_count
