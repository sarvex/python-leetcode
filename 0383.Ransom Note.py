from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        """Check if ransom note can be constructed from magazine using character counting.

        Intuition:
            Each character in the ransom note must appear at least as many
            times in the magazine. Count character frequencies and verify.

        Approach:
            Count character frequencies in the magazine. For each character in
            the ransom note, decrement the count. If any count goes negative,
            the note cannot be constructed.

        Complexity:
            Time: O(m + n) where m and n are the lengths of magazine and ransomNote
            Space: O(1) since there are at most 26 lowercase letters
        """
        char_count = Counter(magazine)
        for char in ransomNote:
            char_count[char] -= 1
            if char_count[char] < 0:
                return False
        return True
