class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        """Binary search on the answer counting values <= mid in multiplication table.

        Intuition:
        Binary search for the smallest value x such that at least k entries in the
        m x n multiplication table are <= x.

        Approach:
        1. Binary search between 1 and m*n.
        2. For each midpoint, count how many entries are <= mid by summing min(mid//i, n)
           for each row i.
        3. Narrow the search range based on the count.

        Complexity:
        Time: O(m * log(m * n))
        Space: O(1)
        """
        left, right = 1, m * n
        while left < right:
            mid = (left + right) >> 1
            count = 0
            for i in range(1, m + 1):
                count += min(mid // i, n)
            if count >= k:
                right = mid
            else:
                left = mid + 1
        return left
