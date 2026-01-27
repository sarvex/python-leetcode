class Solution:
    def findWords(self, words: list[str]) -> list[str]:
        """Filter words that can be typed using one keyboard row.

        Intuition:
            Group the keyboard letters into three rows and check if all
            characters of each word belong to a single row.

        Approach:
            Create sets for each keyboard row. For each word, convert to
            lowercase and check if the character set is a subset of any row.

        Complexity:
            Time: O(n * k) where n is number of words, k is average word length
            Space: O(1)
        """
        row_top = set("qwertyuiop")
        row_middle = set("asdfghjkl")
        row_bottom = set("zxcvbnm")
        result = []
        for word in words:
            chars = set(word.lower())
            if chars <= row_top or chars <= row_middle or chars <= row_bottom:
                result.append(word)
        return result
