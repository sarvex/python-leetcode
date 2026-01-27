class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> list[str]:
        """Find words that follow the bigram (first, second) in text.

        Intuition:
            Scan consecutive triplets of words for the bigram pattern.

        Approach:
            Split text into words, iterate through triplets, and collect the
            third word when the first two match.

        Complexity:
            Time: O(n) where n is the number of words
            Space: O(n) for the split words and result
        """
        words = text.split()
        result: list[str] = []
        for i in range(len(words) - 2):
            word_a, word_b, word_c = words[i : i + 3]
            if word_a == first and word_b == second:
                result.append(word_c)
        return result
