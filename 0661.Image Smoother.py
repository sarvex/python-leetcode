class Solution:
    def imageSmoother(self, img: list[list[int]]) -> list[list[int]]:
        """Average each pixel with its neighbors using brute-force neighborhood scan.

        Intuition:
        For each pixel, compute the average of all valid neighbors (including itself)
        within a 3x3 window centered at that pixel.

        Approach:
        1. For each cell (i, j), iterate over the 3x3 neighborhood.
        2. Sum valid neighbor values and count them.
        3. Store the floor division of sum by count in the result.

        Complexity:
        Time: O(m * n)
        Space: O(m * n)
        """
        rows, cols = len(img), len(img[0])
        result = [[0] * cols for _ in range(rows)]
        for i in range(rows):
            for j in range(cols):
                total = neighbor_count = 0
                for x in range(i - 1, i + 2):
                    for y in range(j - 1, j + 2):
                        if 0 <= x < rows and 0 <= y < cols:
                            neighbor_count += 1
                            total += img[x][y]
                result[i][j] = total // neighbor_count
        return result
