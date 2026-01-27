class Solution:
    def maxProduct(self, words: list[str]) -> int:
        """Bitmask approach to check disjoint character sets efficiently.

        Intuition:
            Represent each word's character set as a bitmask. Two words share
            no common letters if their bitmasks AND to zero.

        Approach:
            1. For each word, compute a 26-bit mask where bit i is set if
               the word contains the i-th letter.
            2. For each pair of words, check if their masks are disjoint.
            3. Track the maximum product of lengths among disjoint pairs.

        Complexity:
            Time: O(n^2 + n*L) where n is number of words, L is average length
            Space: O(n) for the bitmask array
        """
        bitmask = [0] * len(words)
        max_product = 0
        for i, word in enumerate(words):
            for char in word:
                bitmask[i] |= 1 << (ord(char) - ord("a"))
            for j, other in enumerate(words[:i]):
                if (bitmask[i] & bitmask[j]) == 0:
                    max_product = max(max_product, len(word) * len(other))
        return max_product
