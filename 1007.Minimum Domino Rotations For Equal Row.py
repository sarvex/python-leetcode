from math import inf


class Solution:
    def minDominoRotations(self, tops: list[int], bottoms: list[int]) -> int:
        """Find minimum rotations to make all values in one row equal.

        Intuition:
            Only the values on the first domino can possibly fill an entire row.
            Check both candidates and pick the one requiring fewer rotations.

        Approach:
            For a candidate value x, count how many tops and bottoms already
            match. If any domino has neither side equal to x, it is impossible.
            The rotations needed equal n minus the larger of the two counts.

        Complexity:
            Time: O(n) with at most two passes
            Space: O(1)
        """

        def rotations_for(x: int) -> float:
            top_matches = bottom_matches = 0
            for top, bottom in zip(tops, bottoms):
                if x not in (top, bottom):
                    return inf
                top_matches += top == x
                bottom_matches += bottom == x
            return len(tops) - max(top_matches, bottom_matches)

        result = min(rotations_for(tops[0]), rotations_for(bottoms[0]))
        return -1 if result == inf else int(result)
