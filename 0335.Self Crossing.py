class Solution:
    def isSelfCrossing(self, distance: list[int]) -> bool:
        """Check three crossing conditions at each step.

        Intuition:
            A spiral path can self-cross in exactly three geometric patterns
            depending on how the current segment relates to segments 2, 3, 4,
            and 5 steps back.

        Approach:
            1. For each index i >= 3, check if the current segment crosses
               the segment two steps back (basic cross).
            2. For i >= 4, check the special case where the path touches
               itself exactly.
            3. For i >= 5, check the case where the path wraps around and
               overlaps a previous segment.

        Complexity:
            Time: O(n) where n is the length of distance
            Space: O(1)
        """
        for i in range(3, len(distance)):
            if distance[i] >= distance[i - 2] and distance[i - 1] <= distance[i - 3]:
                return True
            if (
                i >= 4
                and distance[i - 1] == distance[i - 3]
                and distance[i] + distance[i - 4] >= distance[i - 2]
            ):
                return True
            if (
                i >= 5
                and distance[i - 2] >= distance[i - 4]
                and distance[i - 1] <= distance[i - 3]
                and distance[i] >= distance[i - 2] - distance[i - 4]
                and distance[i - 1] + distance[i - 5] >= distance[i - 3]
            ):
                return True
        return False
