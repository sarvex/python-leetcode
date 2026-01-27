class Solution:
    def toHexspeak(self, num: str) -> str:
        """Convert a decimal string to hexspeak replacing 0->O and 1->I.

        Intuition:
            Convert to hex, replace digits 0 and 1 with letters O and I.
            The result is valid only if all characters are letters A-F, I, O.

        Approach:
            Convert the number to uppercase hexadecimal, replace '0' with 'O'
            and '1' with 'I', then verify all characters are in the valid set.

        Complexity:
            Time: O(log n)
            Space: O(log n)
        """
        valid_chars = set("ABCDEFIO")
        hexspeak = hex(int(num))[2:].upper().replace("0", "O").replace("1", "I")
        return hexspeak if all(c in valid_chars for c in hexspeak) else "ERROR"
