from bisect import bisect_left
from math import inf


class Solution:
    def makeArrayIncreasing(self, arr1: list[int], arr2: list[int]) -> int:
        """Minimum replacements to make arr1 strictly increasing.

        Intuition:
            Use dynamic programming where we consider replacing consecutive
            elements from arr2 to maintain strict ordering, with sentinel
            values at boundaries.

        Approach:
            Deduplicate and sort arr2. Pad arr1 with -inf and +inf sentinels.
            For each position, either keep the element (if strictly increasing)
            or replace up to k consecutive elements using arr2 values via
            binary search.

        Complexity:
            Time: O(n * m) where n is len(arr1) and m is len(arr2)
            Space: O(n)
        """
        arr2.sort()
        unique_count = 0
        for value in arr2:
            if unique_count == 0 or value != arr2[unique_count - 1]:
                arr2[unique_count] = value
                unique_count += 1
        arr2 = arr2[:unique_count]
        padded = [-inf] + arr1 + [inf]
        length = len(padded)
        dp = [inf] * length
        dp[0] = 0
        for i in range(1, length):
            if padded[i - 1] < padded[i]:
                dp[i] = dp[i - 1]
            j = bisect_left(arr2, padded[i])
            for k in range(1, min(i - 1, j) + 1):
                if padded[i - k - 1] < arr2[j - k]:
                    dp[i] = min(dp[i], dp[i - k - 1] + k)
        return -1 if dp[length - 1] >= inf else dp[length - 1]
