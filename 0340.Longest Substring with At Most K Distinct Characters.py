from collections import Counter


class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        """Sliding window with character frequency counter.

        Intuition:
            Use a sliding window that expands on the right and contracts on
            the left whenever the number of distinct characters exceeds k.

        Approach:
            1. Expand the window by adding characters from the right.
            2. When distinct count exceeds k, shrink from the left by
               decrementing counts and removing zero-count entries.
            3. The answer is the total length minus the left pointer.

        Complexity:
            Time: O(n) where n is the length of s
            Space: O(k) for the counter
        """
        left = 0
        char_count: Counter[str] = Counter()
        for char in s:
            char_count[char] += 1
            if len(char_count) > k:
                char_count[s[left]] -= 1
                if char_count[s[left]] == 0:
                    del char_count[s[left]]
                left += 1
        return len(s) - left
