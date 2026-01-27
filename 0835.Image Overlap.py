from collections import Counter


class Solution:
    def largestOverlap(self, img1: list[list[int]], img2: list[list[int]]) -> int:
        """Count maximum overlap by tracking translation offsets.

        Intuition:
            For every pair of 1-cells between the two images, the translation
            offset is the difference of their coordinates. The most common
            offset gives the maximum overlap.

        Approach:
            1. For each 1-cell in img1 and each 1-cell in img2, compute offset.
            2. Count offset frequencies using a Counter.
            3. Return the maximum count.

        Complexity:
            Time: O(n^4)
            Space: O(n^2)
        """
        size = len(img1)
        offset_count: Counter[tuple[int, int]] = Counter()
        for row1 in range(size):
            for col1 in range(size):
                if img1[row1][col1]:
                    for row2 in range(size):
                        for col2 in range(size):
                            if img2[row2][col2]:
                                offset_count[(row1 - row2, col1 - col2)] += 1
        return max(offset_count.values()) if offset_count else 0
