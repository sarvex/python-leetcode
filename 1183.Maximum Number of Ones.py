class Solution:
    def maximumNumberOfOnes(
        self, width: int, height: int, sideLength: int, maxOnes: int
    ) -> int:
        """Maximize number of ones in a matrix with repeating sub-matrix constraint.

        Intuition:
            The matrix is tiled by sideLength x sideLength sub-matrices. Each cell
            position within the tile appears a certain number of times across the
            full matrix. Greedily pick positions that appear most often.

        Approach:
            For each position in the tile, count how many times it maps across the
            full width x height matrix. Sort these counts in descending order and
            sum the top maxOnes values.

        Complexity:
            Time: O(width * height + sideLength^2 * log(sideLength^2))
            Space: O(sideLength^2)
        """
        tile = sideLength
        counts = [0] * (tile * tile)
        for i in range(width):
            for j in range(height):
                position = (i % tile) * tile + (j % tile)
                counts[position] += 1
        counts.sort(reverse=True)
        return sum(counts[:maxOnes])
