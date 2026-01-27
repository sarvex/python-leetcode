from math import inf


class Solution:
    def minDistance(
        self,
        height: int,
        width: int,
        tree: list[int],
        squirrel: list[int],
        nuts: list[list[int]],
    ) -> int:
        """Minimize total distance for squirrel to collect all nuts to the tree.

        Intuition:
            All nuts except one require a round trip from the tree. The first
            nut the squirrel picks up saves one tree-trip but costs the
            squirrel-to-nut distance. We pick the nut that maximizes the saving.

        Approach:
            1. Compute total round-trip distance from tree to all nuts.
            2. For each nut, calculate the cost if the squirrel picks it first:
               total - tree_dist + squirrel_dist.
            3. Return the minimum such cost.

        Complexity:
            Time: O(n) where n is the number of nuts
            Space: O(1)
        """
        tree_row, tree_col, squirrel_row, squirrel_col = *tree, *squirrel
        total_round_trip = (
            sum(
                abs(nut_row - tree_row) + abs(nut_col - tree_col)
                for nut_row, nut_col in nuts
            )
            * 2
        )
        answer = inf
        for nut_row, nut_col in nuts:
            tree_dist = abs(nut_row - tree_row) + abs(nut_col - tree_col)
            squirrel_dist = (
                abs(nut_row - squirrel_row) + abs(nut_col - squirrel_col) + tree_dist
            )
            answer = min(answer, total_round_trip + squirrel_dist - tree_dist * 2)
        return answer
