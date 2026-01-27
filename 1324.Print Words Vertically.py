class Solution:
    def printVertically(self, s: str) -> list[str]:
        """Print words vertically, reading top to bottom column by column.

        Intuition:
            Transpose the character matrix formed by words, padding shorter
            words with spaces, then strip trailing spaces from each column.

        Approach:
            Split into words, find maximum word length, build each vertical
            string by collecting characters column-wise, and strip trailing spaces.

        Complexity:
            Time: O(w * max_len) where w is number of words
            Space: O(w * max_len)
        """
        words = s.split()
        max_length = max(len(word) for word in words)
        result: list[str] = []
        for col in range(max_length):
            chars = [word[col] if col < len(word) else " " for word in words]
            while chars[-1] == " ":
                chars.pop()
            result.append("".join(chars))
        return result
