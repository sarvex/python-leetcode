class Solution:
    def toLowerCase(self, s: str) -> str:
        """Bitwise OR to convert uppercase to lowercase.

        Intuition:
            ASCII uppercase letters differ from lowercase by bit 5 (value 32).
            Setting bit 5 via OR with 32 converts uppercase to lowercase.

        Approach:
            Iterate through each character, if uppercase apply bitwise OR with
            32 to shift to lowercase, otherwise keep the character unchanged.

        Complexity:
            Time: O(n) where n is the length of the string
            Space: O(n) for the resulting string
        """
        return "".join([chr(ord(char) | 32) if char.isupper() else char for char in s])
