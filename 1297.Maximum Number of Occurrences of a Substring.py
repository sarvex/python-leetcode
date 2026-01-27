from collections import Counter


class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        """Maximum frequency of a substring meeting letter and size constraints.

        Intuition:
            Only substrings of minSize matter because any valid longer substring
            contains a valid shorter one with at least the same frequency.

        Approach:
            Slide a window of minSize across the string. For each window, check if
            the number of distinct characters is within maxLetters, and track the
            frequency of qualifying substrings.

        Complexity:
            Time: O(n * minSize)
            Space: O(n)
        """
        max_frequency = 0
        substring_count: Counter[str] = Counter()
        for i in range(len(s) - minSize + 1):
            substring = s[i : i + minSize]
            if len(set(substring)) <= maxLetters:
                substring_count[substring] += 1
                max_frequency = max(max_frequency, substring_count[substring])
        return max_frequency
