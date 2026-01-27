class Solution:
    def isSolvable(self, words: list[str], result: str) -> bool:
        """Determine if a verbal arithmetic puzzle has a valid digit assignment.

        Intuition:
            Backtracking with column-by-column evaluation avoids generating all
            permutations and prunes early on invalid partial assignments.

        Approach:
            Process the equation column by column (right to left). For each letter,
            try assigning unused digits (respecting no leading zeros). Propagate
            carry and validate at each column boundary.

        Complexity:
            Time: O(10! * max_columns) in worst case
            Space: O(number of unique letters)
        """
        if max(map(len, words)) > len(result):
            return False

        words.append(result)
        digits_used = [0] * 10
        letter_to_digit: dict[str, int] = {}

        def backtrack(word_index: int, column: int, carry: int) -> bool:
            if column == len(result):
                return carry == 0
            if word_index == len(words):
                return carry % 10 == 0 and backtrack(0, column + 1, carry // 10)

            if column >= len(words[word_index]):
                return backtrack(word_index + 1, column, carry)

            letter = words[word_index][~column]
            sign = -1 if word_index + 1 == len(words) else 1

            if letter in letter_to_digit:
                digit = letter_to_digit[letter]
                if column and column + 1 == len(words[word_index]) and digit == 0:
                    return False
                return backtrack(word_index + 1, column, carry + sign * digit)

            for digit, used in enumerate(digits_used):
                if not used and (
                    digit or column == 0 or column + 1 < len(words[word_index])
                ):
                    letter_to_digit[letter] = digit
                    digits_used[digit] = 1
                    if backtrack(word_index + 1, column, carry + sign * digit):
                        return True
                    digits_used[digit] = 0
                    del letter_to_digit[letter]
            return False

        return backtrack(0, 0, 0)
