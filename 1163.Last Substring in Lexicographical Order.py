class Solution:
    def lastSubstring(self, s: str) -> str:
        """Find the lexicographically largest substring using two-pointer comparison.

        Intuition:
            The largest substring must start at some index. We compare two candidate
            starting positions, advancing past matching prefixes.

        Approach:
            Use two pointers i and j with a match length k. Compare characters
            at i+k and j+k, advancing the losing pointer past the matched prefix.
            The winner at pointer i gives the starting index of the result.

        Complexity:
            Time: O(n)
            Space: O(1)
        """
        i, j, match_len = 0, 1, 0
        while j + match_len < len(s):
            if s[i + match_len] == s[j + match_len]:
                match_len += 1
            elif s[i + match_len] < s[j + match_len]:
                i += match_len + 1
                match_len = 0
                if i >= j:
                    j = i + 1
            else:
                j += match_len + 1
                match_len = 0
        return s[i:]
