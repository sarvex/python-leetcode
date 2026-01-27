from functools import cache

from sortedcontainers import SortedDict


class Solution:
    def oddEvenJumps(self, arr: list[int]) -> int:
        """Memoized search with sorted dictionary to find valid odd/even jump targets.

        Intuition:
        From each index, odd jumps go to the smallest value >= current, and
        even jumps go to the largest value <= current. A sorted dictionary
        enables efficient lookup of these targets when scanning right to left.

        Approach:
        1. Build a jump graph: for each index, find the next odd and even jump targets
        2. Use a SortedDict scanning from right to left for efficient bisection
        3. Memoized DFS alternates between odd and even jumps
        4. Count starting indices that can reach the last index

        Complexity:
        Time: O(n log n) for sorted dictionary operations
        Space: O(n) for the jump graph and memoization cache
        """
        length = len(arr)
        jump_targets = [[0] * 2 for _ in range(length)]
        sorted_dict: SortedDict = SortedDict()

        for index in range(length - 1, -1, -1):
            odd_pos = sorted_dict.bisect_left(arr[index])
            jump_targets[index][1] = (
                sorted_dict.values()[odd_pos] if odd_pos < len(sorted_dict) else -1
            )
            even_pos = sorted_dict.bisect_right(arr[index]) - 1
            jump_targets[index][0] = (
                sorted_dict.values()[even_pos] if even_pos >= 0 else -1
            )
            sorted_dict[arr[index]] = index

        @cache
        def can_reach_end(position: int, is_odd_jump: int) -> bool:
            if position == length - 1:
                return True
            if jump_targets[position][is_odd_jump] == -1:
                return False
            return can_reach_end(jump_targets[position][is_odd_jump], is_odd_jump ^ 1)

        return sum(can_reach_end(i, 1) for i in range(length))
