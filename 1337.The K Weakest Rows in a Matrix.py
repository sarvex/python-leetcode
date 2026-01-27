from bisect import bisect_right


class Solution:
    def kWeakestRows(self, mat: list[list[int]], k: int) -> list[int]:
        """Return indices of k weakest rows (fewest soldiers) in the matrix.

        Intuition:
            Count soldiers per row using binary search on the sorted row
            (1s before 0s), then sort row indices by soldier count.

        Approach:
            For each row, count soldiers via bisect on the reversed row.
            Sort indices by soldier count (ties broken by index) and return first k.

        Complexity:
            Time: O(m * log(n) + m * log(m))
            Space: O(m)
        """
        rows, cols = len(mat), len(mat[0])
        soldier_counts = [cols - bisect_right(row[::-1], 0) for row in mat]
        indices = sorted(range(rows), key=lambda i: soldier_counts[i])
        return indices[:k]
