class Solution:
    def hIndex(self, citations: list[int]) -> int:
        """Binary search on sorted citations to find the h-index.

        Intuition:
            Since citations are sorted, binary search can efficiently find the
            largest h such that at least h papers have h or more citations.

        Approach:
            1. Use binary search on the range [0, n].
            2. For a candidate mid, check if citations[n - mid] >= mid.
            3. If true, search higher; otherwise search lower.
            4. Return the converged value as the h-index.

        Complexity:
            Time: O(log n) where n is the number of papers
            Space: O(1)
        """
        total = len(citations)
        left, right = 0, total
        while left < right:
            mid = (left + right + 1) >> 1
            if citations[total - mid] >= mid:
                left = mid
            else:
                right = mid - 1
        return left
