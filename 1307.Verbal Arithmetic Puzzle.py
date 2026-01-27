class Solution:
    def isSolvable(self, words: list[str], result: str) -> bool:
        """Determine if a verbal arithmetic puzzle has a valid digit assignment.

        Intuition:
            Backtracking column by column with digit-to-letter and letter-to-digit
            mappings allows early pruning of invalid assignments.

        Approach:
            Append result to words. Process column by column (right to left).
            For mapped letters, use existing assignments. For unmapped letters,
            try all available digits respecting no-leading-zero constraint.
            Validate carry propagation at column boundaries.

        Complexity:
            Time: O(10! * max_columns) in worst case
            Space: O(number of unique letters)
        """
        words.append(result)
        total_rows = len(words)
        total_cols = max(len(word) for word in words)
        letter_to_digit: dict[str, int] = {}
        digit_to_letter = ["-"] * 10

        return self._find_mapping(
            words, 0, 0, 0, letter_to_digit, digit_to_letter, total_rows, total_cols
        )

    def _find_mapping(
        self,
        words: list[str],
        row: int,
        col: int,
        balance: int,
        letter_to_digit: dict[str, int],
        digit_to_letter: list[str],
        total_rows: int,
        total_cols: int,
    ) -> bool:
        if col == total_cols:
            return balance == 0

        if row == total_rows:
            return balance % 10 == 0 and self._find_mapping(
                words,
                0,
                col + 1,
                balance // 10,
                letter_to_digit,
                digit_to_letter,
                total_rows,
                total_cols,
            )

        word = words[row]

        if col >= len(word):
            return self._find_mapping(
                words,
                row + 1,
                col,
                balance,
                letter_to_digit,
                digit_to_letter,
                total_rows,
                total_cols,
            )

        letter = word[len(word) - 1 - col]
        sign = 1 if row < total_rows - 1 else -1

        if letter in letter_to_digit and (
            letter_to_digit[letter] != 0
            or (letter_to_digit[letter] == 0 and len(word) == 1)
            or col != len(word) - 1
        ):
            return self._find_mapping(
                words,
                row + 1,
                col,
                balance + sign * letter_to_digit[letter],
                letter_to_digit,
                digit_to_letter,
                total_rows,
                total_cols,
            )

        for digit in range(10):
            is_valid_digit = digit_to_letter[digit] == "-" and (
                digit != 0 or (digit == 0 and len(word) == 1) or col != len(word) - 1
            )
            if is_valid_digit:
                digit_to_letter[digit] = letter
                letter_to_digit[letter] = digit

                if self._find_mapping(
                    words,
                    row + 1,
                    col,
                    balance + sign * letter_to_digit[letter],
                    letter_to_digit,
                    digit_to_letter,
                    total_rows,
                    total_cols,
                ):
                    return True

                digit_to_letter[digit] = "-"
                if letter in letter_to_digit:
                    del letter_to_digit[letter]

        return False
