from collections import defaultdict

class Solution:
    def maxFreqSum(self, s: str) -> int:
        """Tagline: defaultdict frequency count + max tracking per group.

        Intuition:
            We only need the maximum frequency among vowels and among consonants. Count each
            character once, then determine the maximum for each group.

        Approach:
            - Count characters with defaultdict(int) in one pass.
            - Use a constant-time membership set for vowels.
            - Sweep the frequency map to track the max vowel and consonant counts.
            - Return the sum of both maxima.
            
        Complexity:
            Time: O(n)
            Space: O(1) — at most 26 keys in the map
        """
        VOWELS = {"a", "e", "i", "o", "u"}
        freq_map = defaultdict(int)
        for ch in s:
            freq_map[ch] += 1

        vowel_max = 0
        consonant_max = 0
        for ch, cnt in freq_map.items():
            if ch in VOWELS:
                if cnt > vowel_max:
                    vowel_max = cnt
            else:
                if cnt > consonant_max:
                    consonant_max = cnt

        return vowel_max + consonant_max