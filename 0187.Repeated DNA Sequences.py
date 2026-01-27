from collections import Counter


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> list[str]:
        """Sliding Window with Counter Approach

        Intuition:
            Use a sliding window of length 10 to extract all substrings
            and count occurrences to find those appearing more than once.

        Approach:
            1. Slide a window of size 10 across the string.
            2. Count each 10-character substring using a Counter.
            3. When a substring's count reaches exactly 2, add it to results.

        Complexity:
            Time: O(n) where n is the length of the string
            Space: O(n) for the counter storing all 10-length substrings
        """
        frequency: Counter[str] = Counter()
        result: list[str] = []
        for i in range(len(s) - 10 + 1):
            substring = s[i : i + 10]
            frequency[substring] += 1
            if frequency[substring] == 2:
                result.append(substring)
        return result
