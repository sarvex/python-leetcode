class Solution:
    def maxDistToClosest(self, seats: list[int]) -> int:
        """Track first and last occupied seats and max gap between them.

        Intuition:
            The best seat is either at the start (before first person), at the
            end (after last person), or in the middle of the largest gap.

        Approach:
            1. Find the first and last occupied seat indices.
            2. Track the maximum gap between consecutive occupied seats.
            3. The answer is max(first_occupied, n - 1 - last_occupied, max_gap // 2).

        Complexity:
            Time: O(n)
            Space: O(1)
        """
        first_occupied = last_occupied = None
        max_gap = 0
        for i, occupied in enumerate(seats):
            if occupied:
                if last_occupied is not None:
                    max_gap = max(max_gap, i - last_occupied)
                if first_occupied is None:
                    first_occupied = i
                last_occupied = i
        return max(first_occupied, len(seats) - last_occupied - 1, max_gap // 2)
