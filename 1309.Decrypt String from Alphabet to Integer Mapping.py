class Solution:
    def freqAlphabets(self, s: str) -> str:
        """Decrypt string from alphabet to integer mapping.

        Intuition:
            Characters followed by '#' represent two-digit numbers (10-26),
            while standalone digits represent single-digit numbers (1-9).

        Approach:
            Iterate through the string. If the character two positions ahead is '#',
            decode a two-digit number; otherwise decode a single digit. Map each
            number to the corresponding lowercase letter.

        Complexity:
            Time: O(n)
            Space: O(n)
        """

        def decode(numeric_str: str) -> str:
            return chr(ord("a") + int(numeric_str) - 1)

        index, length = 0, len(s)
        result: list[str] = []
        while index < length:
            if index + 2 < length and s[index + 2] == "#":
                result.append(decode(s[index : index + 2]))
                index += 3
            else:
                result.append(decode(s[index]))
                index += 1
        return "".join(result)
