class Solution:
    def sortVowels(self, s: str) -> str:
        """Tagline: Extract, sort, and reinsert vowels while keeping consonants fixed.

        Intuition:
            Only vowels move when sorting; consonants must remain in their original
            positions. Therefore, gather vowels, sort them, then scan the string
            again and replace each vowel slot with the next smallest vowel.

        Approach:
            - Use a constant-time membership set of vowels (both cases).
            - Extract all vowels from the input string and sort them using Python's
              default character ordering.
            - Iterate the original characters and, whenever a vowel is encountered,
              replace it with the next value from the sorted vowels iterator.
            - Join and return the reconstructed list of characters.

        Complexity:
            - Time: O(n log n) due to sorting k vowels where k ≤ n; the scans are O(n).
            - Space: O(k) to store the vowels being sorted.
        """

        VOWELS = set("AEIOUaeiou")

        vowels = sorted([ch for ch in s if ch in VOWELS])
        v_iter = iter(vowels)

        chars = list(s)
        for i, ch in enumerate(chars):
            if ch in VOWELS:
                chars[i] = next(v_iter)
        return "".join(chars)
