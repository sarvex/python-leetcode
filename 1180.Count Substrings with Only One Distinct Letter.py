class Solution:
    def countLetters(self, s: str) -> int:
        """Count substrings containing only one distinct letter.

        Intuition:
            Consecutive runs of the same character each contribute a triangular
            number of valid substrings.

        Approach:
            Scan through the string identifying runs of identical characters.
            For a run of length L, the number of single-character substrings
            is L * (L + 1) / 2.

        Complexity:
            Time: O(n)
            Space: O(1)
        """
        n = len(s)
        left = 0
        total = 0
        while left < n:
            right = left
            while right < n and s[right] == s[left]:
                right += 1
            run_length = right - left
            total += (1 + run_length) * run_length // 2
            left = right
        return total
