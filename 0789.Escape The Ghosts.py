class Solution:
    def escapeGhosts(self, ghosts: list[list[int]], target: list[int]) -> bool:
        """Compare Manhattan distances of player and all ghosts to the target.

        Intuition:
            The player can escape only if no ghost can reach the target in the
            same or fewer steps. Since both move optimally in a grid, Manhattan
            distance determines who arrives first.

        Approach:
            1. Compute the player's Manhattan distance from origin to target
            2. For each ghost, compute its Manhattan distance to the target
            3. If any ghost distance <= player distance, escape is impossible

        Complexity:
            Time: O(g) where g is the number of ghosts
            Space: O(1)
        """
        target_x, target_y = target
        player_distance = abs(target_x) + abs(target_y)
        return all(
            abs(target_x - ghost_x) + abs(target_y - ghost_y) > player_distance
            for ghost_x, ghost_y in ghosts
        )
