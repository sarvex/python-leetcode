class Solution:
    def firstBadVersion(self, n: int) -> int:
        """Binary search to find the first bad version.

        Intuition:
            The versions form a monotonic sequence where all good versions come
            before all bad versions. Binary search efficiently finds the boundary.

        Approach:
            1. Set search bounds to [1, n].
            2. Check the midpoint with isBadVersion.
            3. If mid is bad, the first bad version is at mid or earlier.
            4. If mid is good, the first bad version is after mid.
            5. Return left when the bounds converge.

        Complexity:
            Time: O(log n)
            Space: O(1)
        """
        left, right = 1, n
        while left < right:
            mid = (left + right) >> 1
            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1
        return left
