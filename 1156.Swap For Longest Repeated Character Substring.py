from collections import Counter


class Solution:
    def maxRepOpt1(self, text: str) -> int:
        """Find longest repeated character substring with at most one swap.

        Intuition:
            For each run of identical characters, check if we can extend it by
            bridging over a single different character to merge with the next
            same-character run.

        Approach:
            Scan through runs of same characters. For each run, look past one
            different character to see if the next run has the same character.
            The merged length is capped by the total count of that character.

        Complexity:
            Time: O(n)
            Space: O(1) — character frequency array of size 26
        """
        char_count = Counter(text)
        length = len(text)
        result = 0
        i = 0
        while i < length:
            j = i
            while j < length and text[j] == text[i]:
                j += 1
            left_run = j - i
            k = j + 1
            while k < length and text[k] == text[i]:
                k += 1
            right_run = k - j - 1
            result = max(result, min(left_run + right_run + 1, char_count[text[i]]))
            i = j
        return result
