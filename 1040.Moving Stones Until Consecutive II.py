class Solution:
    def numMovesStonesII(self, stones: list[int]) -> list[int]:
        """Moving Stones Until Consecutive II using sliding window.

        Intuition:
            The maximum moves use the larger of the two endpoint gaps. The
            minimum moves use a sliding window of size n to find the densest
            window, with a special case for near-consecutive arrangements.

        Approach:
            Sort stones. Maximum is max of (stones[-1] - stones[1] + 1,
            stones[-2] - stones[0] + 1) minus (n-1). For minimum, slide a
            window of size n over sorted positions. Handle the edge case where
            n-1 stones are consecutive but one is isolated.

        Complexity:
            Time: O(n log n)
            Space: O(1) excluding sort
        """
        stones.sort()
        count = len(stones)
        max_moves = max(
            stones[-1] - stones[1] + 1,
            stones[-2] - stones[0] + 1,
        ) - (count - 1)
        min_moves = count
        left = 0
        for right, position in enumerate(stones):
            while position - stones[left] + 1 > count:
                left += 1
            window_size = right - left + 1
            if window_size == count - 1 and position - stones[left] == count - 2:
                min_moves = min(min_moves, 2)
            else:
                min_moves = min(min_moves, count - window_size)
        return [min_moves, max_moves]
