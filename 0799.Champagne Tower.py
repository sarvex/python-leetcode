class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        """Simulate champagne overflow using dynamic programming.

        Intuition:
            Each glass overflows equally to the two glasses below it. We can
            simulate row by row, tracking how much champagne each glass holds.

        Approach:
            1. Initialize the top glass with the poured amount.
            2. For each row, if a glass has more than 1 unit, split the excess
               equally to the two glasses below, then cap the glass at 1.
            3. Return the value at the queried position.

        Complexity:
            Time: O(query_row^2)
            Space: O(query_row^2)
        """
        glasses = [[0] * 101 for _ in range(101)]
        glasses[0][0] = poured
        for i in range(query_row + 1):
            for j in range(i + 1):
                if glasses[i][j] > 1:
                    overflow = (glasses[i][j] - 1) / 2
                    glasses[i][j] = 1
                    glasses[i + 1][j] += overflow
                    glasses[i + 1][j + 1] += overflow
        return glasses[query_row][query_glass]
