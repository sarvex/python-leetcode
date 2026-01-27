import math
from collections import Counter


class Solution:
    def numRabbits(self, answers: list[int]) -> int:
        """Group rabbits by answer and compute minimum population per group.

        Intuition:
            If a rabbit says k, it belongs to a group of k+1 same-colored rabbits.
            Multiple rabbits giving the same answer may or may not be in the same
            group, so we need ceil(count / (k+1)) groups of size k+1.

        Approach:
            1. Count frequency of each answer
            2. For each answer k with count v, compute ceil(v / (k+1)) * (k+1)
            3. Sum all group sizes

        Complexity:
            Time: O(n) where n is the number of answers
            Space: O(n) for the counter
        """
        freq = Counter(answers)
        return sum(
            math.ceil(count / (answer + 1)) * (answer + 1)
            for answer, count in freq.items()
        )
