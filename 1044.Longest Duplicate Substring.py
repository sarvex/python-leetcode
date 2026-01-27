class Solution:
    def longestDupSubstring(self, s: str) -> str:
        """Longest Duplicate Substring using binary search on length.

        Intuition:
            If a duplicate substring of length L exists, then one of length
            L-1 also exists. This monotonic property enables binary search.

        Approach:
            Binary search on the length of the duplicate substring. For each
            candidate length, use a sliding window with a hash set to check
            if any substring of that length appears more than once.

        Complexity:
            Time: O(n^2 * log n) worst case with string hashing
            Space: O(n^2) for storing substrings in the set
        """

        def find_duplicate(length: int) -> str:
            seen: set[str] = set()
            for i in range(total_length - length + 1):
                substring = s[i : i + length]
                if substring in seen:
                    return substring
                seen.add(substring)
            return ""

        total_length = len(s)
        left, right = 0, total_length
        result = ""
        while left < right:
            mid = (left + right + 1) >> 1
            candidate = find_duplicate(mid)
            result = candidate or result
            if candidate:
                left = mid
            else:
                right = mid - 1
        return result
