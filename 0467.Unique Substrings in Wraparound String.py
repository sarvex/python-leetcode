from collections import defaultdict


class Solution:
    def findSubstringInWraproundString(self, s: str) -> int:
        """Track max consecutive wraparound length ending at each character.

        Intuition:
            Any substring of s that is a contiguous segment in the infinite
            wraparound string 'abcde...xyzabc...' is uniquely determined by
            its ending character and length. Track the longest such segment
            ending at each character.

        Approach:
            Iterate through s, maintaining a running length of consecutive
            wraparound characters. For each character, update the maximum
            length seen ending at that character. The answer is the sum of
            all maximum lengths.

        Complexity:
            Time: O(n)
            Space: O(1) — at most 26 entries
        """
        max_length_at = defaultdict(int)
        consecutive = 0
        for i, char in enumerate(s):
            if i and (ord(char) - ord(s[i - 1])) % 26 == 1:
                consecutive += 1
            else:
                consecutive = 1
            max_length_at[char] = max(max_length_at[char], consecutive)
        return sum(max_length_at.values())
