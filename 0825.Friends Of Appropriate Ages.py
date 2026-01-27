from collections import Counter


class Solution:
    def numFriendRequests(self, ages: list[int]) -> int:
        """Count friend requests using age frequency counting.

        Intuition:
            With ages in [1, 120], iterate over all age pairs and check the
            friend request conditions using frequency counts.

        Approach:
            1. Count the frequency of each age.
            2. For each pair of ages (i, j), check if a request from i to j is valid.
            3. Multiply by counts; subtract self-requests when i == j.

        Complexity:
            Time: O(120^2) = O(1)
            Space: O(120) = O(1)
        """
        age_count = Counter(ages)
        result = 0
        for age_a in range(1, 121):
            count_a = age_count[age_a]
            for age_b in range(1, 121):
                count_b = age_count[age_b]
                if not (
                    age_b <= 0.5 * age_a + 7
                    or age_b > age_a
                    or (age_b > 100 and age_a < 100)
                ):
                    result += count_a * count_b
                    if age_a == age_b:
                        result -= count_b
        return result
