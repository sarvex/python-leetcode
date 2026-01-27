from itertools import accumulate


class Solution:
    def getModifiedArray(self, length: int, updates: list[list[int]]) -> list[int]:
        """Apply range updates efficiently using a difference array.

        Intuition:
            Instead of applying each update to every element in the range,
            use a difference array where each update only modifies two endpoints.
            The final array is obtained via prefix sum.

        Approach:
            Create a difference array of zeros. For each update (start, end, val),
            add val at start and subtract val at end+1 (if in bounds). Finally,
            compute the prefix sum of the difference array to get the result.

        Complexity:
            Time: O(n + k) where k is the number of updates
            Space: O(n)
        """
        diff = [0] * length
        for start, end, val in updates:
            diff[start] += val
            if end + 1 < length:
                diff[end + 1] -= val
        return list(accumulate(diff))
