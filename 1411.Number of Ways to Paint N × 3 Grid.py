class Solution:
    def numOfWays(self, n: int) -> int:
        """Count ways to paint an n x 3 grid with 3 colors, no adjacent same.

        Intuition:
            Each row has two pattern types: 2-color (ABA) and 3-color (ABC).
            Track transitions between these pattern types across rows.

        Approach:
            Start with 6 patterns of each type for the first row. For each
            subsequent row, a 2-color pattern generates 3 two-color and 2
            three-color successors; a 3-color pattern generates 2 of each.

        Complexity:
            Time: O(n) iterating through rows
            Space: O(1) tracking two counts
        """
        modulus = 10**9 + 7
        two_color = 6
        three_color = 6

        for _ in range(n - 1):
            new_two_color = (3 * two_color + 2 * three_color) % modulus
            new_three_color = (2 * two_color + 2 * three_color) % modulus
            two_color, three_color = new_two_color, new_three_color

        return (two_color + three_color) % modulus
