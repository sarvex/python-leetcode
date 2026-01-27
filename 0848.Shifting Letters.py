from string import ascii_lowercase


class Solution:
    def shiftingLetters(self, s: str, shifts: list[int]) -> str:
        """Apply cumulative shifts using a difference array.

        Intuition:
            Each shift[i] affects all characters from 0 to i. Using a
            difference array, we can efficiently compute the total shift
            for each position.

        Approach:
            1. Build a difference array from the original character values.
            2. Apply each shift to the difference array.
            3. Reconstruct the string using prefix sums modulo 26.

        Complexity:
            Time: O(n)
            Space: O(n)
        """
        length = len(s)
        diff = [0] * (length + 1)
        for i, char in enumerate(s):
            char_value = ord(char) - ord("a")
            diff[i] += char_value
            diff[i + 1] -= char_value
        for i, shift in enumerate(shifts):
            diff[0] += shift
            diff[i + 1] -= shift
        result: list[str] = []
        for i in range(length):
            diff[i] %= 26
            result.append(ascii_lowercase[diff[i]])
            diff[i + 1] += diff[i]
        return "".join(result)
