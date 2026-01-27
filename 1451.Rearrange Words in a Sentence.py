class Solution:
    def arrangeWords(self, text: str) -> str:
        """Rearrange words in sentence by ascending length, preserving order for ties.

        Intuition:
            Sort words by length using a stable sort to preserve relative order
            of equal-length words.

        Approach:
            Split the text into words, lowercase the first word, sort by length,
            capitalize the first word of the result, and rejoin.

        Complexity:
            Time: O(n log n) for sorting
            Space: O(n) for the word list
        """
        words = text.split()
        words[0] = words[0].lower()
        words.sort(key=len)
        words[0] = words[0].title()
        return " ".join(words)
