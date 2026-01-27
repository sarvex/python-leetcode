from collections import Counter
from math import dist


class Solution:
    def numberOfBoomerangs(self, points: list[list[int]]) -> int:
        """Count equidistant point pairs using distance frequency counting.

        Intuition:
            For each point, count how many other points are at each distance.
            Each pair at the same distance can form a boomerang in two orderings.

        Approach:
            1. For each anchor point, compute distances to all other points.
            2. Track distance frequencies in a counter.
            3. For each distance with count c, there are c*(c-1) ordered pairs,
               but we accumulate incrementally: add current count before incrementing.
            4. Multiply the total by 2 for the two orderings.

        Complexity:
            Time: O(n^2) for all pairs of points.
            Space: O(n) for the distance counter.
        """
        total = 0
        for anchor in points:
            distance_count = Counter()
            for other in points:
                distance = dist(anchor, other)
                total += distance_count[distance]
                distance_count[distance] += 1
        return total << 1
