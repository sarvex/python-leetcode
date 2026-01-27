class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        """Two-pointer validation of word abbreviation.

        Intuition:
            Walk through both strings simultaneously. When a digit is
            encountered in the abbreviation, accumulate the number and
            skip that many characters in the word.

        Approach:
            1. Use two pointers for word and abbreviation, plus an accumulator.
            2. If the current abbr character is a digit, accumulate the number.
               Leading zeros are invalid.
            3. If it is a letter, advance the word pointer by the accumulated
               skip count, reset the accumulator, and compare characters.
            4. At the end, verify both pointers reached their respective ends.

        Complexity:
            Time: O(n) where n is the length of the abbreviation
            Space: O(1)
        """
        word_len, abbr_len = len(word), len(abbr)
        word_index = abbr_index = skip_count = 0
        while word_index < word_len and abbr_index < abbr_len:
            if abbr[abbr_index].isdigit():
                if abbr[abbr_index] == "0" and skip_count == 0:
                    return False
                skip_count = skip_count * 10 + int(abbr[abbr_index])
            else:
                word_index += skip_count
                skip_count = 0
                if word_index >= word_len or word[word_index] != abbr[abbr_index]:
                    return False
                word_index += 1
            abbr_index += 1
        return word_index + skip_count == word_len and abbr_index == abbr_len
