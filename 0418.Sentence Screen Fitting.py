class Solution:
    def wordsTyping(self, sentence: list[str], rows: int, cols: int) -> int:
        """Simulate screen fitting using a concatenated sentence string.

        Intuition:
            Join all words with spaces into a repeating string. For each row,
            advance by cols characters and adjust the cursor to land on a word
            boundary.

        Approach:
            1. Concatenate the sentence with trailing space into one string.
            2. For each row, advance cursor by cols.
            3. If the cursor lands on a space, move forward by one.
            4. Otherwise, backtrack until the previous character is a space.
            5. The number of complete sentences is cursor // string_length.

        Complexity:
            Time: O(rows * max_word_length) in the worst case.
            Space: O(total_chars) for the concatenated string.
        """
        joined = " ".join(sentence) + " "
        joined_length = len(joined)
        cursor = 0
        for _ in range(rows):
            cursor += cols
            if joined[cursor % joined_length] == " ":
                cursor += 1
            while cursor and joined[(cursor - 1) % joined_length] != " ":
                cursor -= 1
        return cursor // joined_length
