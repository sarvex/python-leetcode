from functools import cache


class Solution:
    def canCross(self, stones: list[int]) -> bool:
        """DFS with memoization checking reachability of last stone.

        Intuition:
            From each stone, the frog can jump k-1, k, or k+1 units where
            k was the last jump size. We can memoize the state (stone index,
            last jump) to avoid redundant exploration.

        Approach:
            1. Build a position-to-index map for O(1) stone lookup.
            2. DFS from stone 0 with jump size 0.
            3. At each stone, try jumps of size k-1, k, k+1 (if > 0).
            4. Check if the target position exists in the stone set.
            5. Return True if the last stone is reached.

        Complexity:
            Time: O(n^2) where n is the number of stones
            Space: O(n^2) for memoization cache
        """

        @cache
        def dfs(index: int, last_jump: int) -> bool:
            if index == stone_count - 1:
                return True
            for jump_size in range(last_jump - 1, last_jump + 2):
                if (
                    jump_size > 0
                    and stones[index] + jump_size in position_map
                    and dfs(position_map[stones[index] + jump_size], jump_size)
                ):
                    return True
            return False

        stone_count = len(stones)
        position_map = {stone: i for i, stone in enumerate(stones)}
        return dfs(0, 0)
