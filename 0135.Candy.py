from typing import List

class Solution:
    def candy(self, ratings: List[int]) -> int:
        """Two-pass greedy approach to distribute candies

        Intuition:
        When a child has a higher rating than their neighbor, they should get more candies.
        We can solve this by making two passes through the array - one from left to right
        and another from right to left.

        Approach:
        1. Initialize two arrays (left and right) with all 1's (minimum candy requirement)
        2. Left-to-right pass: If current rating > previous rating, give current child
        one more candy than the previous child
        3. Right-to-left pass: If current rating > next rating, ensure current child
        has more candies than the next child
        4. For each position, take the maximum of left and right arrays to satisfy
        both neighbor conditions
        5. Sum all values to get the minimum total candies needed

        Complexity:
        Time: O(n) where n is the length of the ratings array
        Space: O(n) for the two auxiliary arrays
        """
        n = len(ratings)
        left = [1] * n
        right = [1] * n

        # Left to right pass
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                left[i] = left[i - 1] + 1

        # Right to left pass
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                right[i] = right[i + 1] + 1

        # Take maximum at each position and sum
        return sum(max(a, b) for a, b in zip(left, right))
