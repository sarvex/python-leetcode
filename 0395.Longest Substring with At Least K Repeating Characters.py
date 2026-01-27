from collections import Counter


class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        """Divide and conquer splitting on infrequent characters.

        Intuition:
            Any character appearing fewer than k times cannot be part
            of a valid substring, so we can split on such characters
            and recursively solve each segment.

        Approach:
            1. Count character frequencies in the current range.
            2. Find a character with count < k to use as a split point.
            3. If no such character exists, the entire range is valid.
            4. Otherwise, split the range at occurrences of that character
               and recursively find the longest valid substring in each part.

        Complexity:
            Time: O(n * 26) since we recurse at most 26 levels
            Space: O(26^2) for recursion stack and counters
        """

        def dfs(left: int, right: int) -> int:
            frequency = Counter(s[left : right + 1])
            split_char = next(
                (char for char, count in frequency.items() if count < k), ""
            )
            if not split_char:
                return right - left + 1
            i = left
            max_length = 0
            while i <= right:
                while i <= right and s[i] == split_char:
                    i += 1
                if i >= right:
                    break
                j = i
                while j <= right and s[j] != split_char:
                    j += 1
                segment_length = dfs(i, j - 1)
                max_length = max(max_length, segment_length)
                i = j
            return max_length

        return dfs(0, len(s) - 1)
