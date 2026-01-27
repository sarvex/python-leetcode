class Solution:
    def validWordSquare(self, words: list[str]) -> bool:
        """Check that the i-th row equals the i-th column character by character.

        Intuition:
            A valid word square requires words[i][j] == words[j][i] for all
            valid positions. We must also handle ragged rows gracefully.

        Approach:
            1. Iterate through each word and each character.
            2. Check bounds: j must be within the number of words, and i must
               be within the length of words[j].
            3. Compare words[i][j] with words[j][i]; return False on mismatch.

        Complexity:
            Time: O(m * max_len) where m is the number of words.
            Space: O(1) using no extra data structures.
        """
        num_words = len(words)
        for row, word in enumerate(words):
            for col, char in enumerate(word):
                if (
                    col >= num_words
                    or row >= len(words[col])
                    or char != words[col][row]
                ):
                    return False
        return True
