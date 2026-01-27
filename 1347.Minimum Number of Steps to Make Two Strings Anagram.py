from collections import Counter


class Solution:
    def minSteps(self, s: str, t: str) -> int:
        """Find minimum character replacements to make t an anagram of s.

        Intuition:
            Count characters in s. For each character in t that can be matched
            to s, decrement the count. Unmatched characters need replacement.

        Approach:
            Build a frequency counter for s. Iterate through t, decrementing
            available counts. Characters in t not covered by s contribute to
            the replacement count.

        Complexity:
            Time: O(n)
            Space: O(1) since alphabet size is fixed
        """
        frequency = Counter(s)
        replacements = 0
        for char in t:
            if frequency[char] > 0:
                frequency[char] -= 1
            else:
                replacements += 1
        return replacements
