from collections import Counter


class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        """Sliding Window with Character Count.

        Intuition:
            Use a sliding window that expands to include characters and
            contracts when more than two distinct characters are present.

        Approach:
            Maintain a counter for characters in the current window. Expand
            the right boundary one character at a time. When the number of
            distinct characters exceeds two, shrink the window from the left
            until at most two distinct characters remain.

        Complexity:
            Time: O(n) each character is added and removed at most once
            Space: O(1) counter holds at most 3 distinct characters
        """
        char_count: Counter[str] = Counter()
        result = left = 0
        for right, char in enumerate(s):
            char_count[char] += 1
            while len(char_count) > 2:
                char_count[s[left]] -= 1
                if char_count[s[left]] == 0:
                    char_count.pop(s[left])
                left += 1
            result = max(result, right - left + 1)
        return result
