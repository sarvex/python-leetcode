class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        """Reverse traversal with modular arithmetic to find the kth character.

        Intuition:
            Instead of building the decoded string, compute its total length
            then work backwards, using modular arithmetic to reduce k until
            we find the target character.

        Approach:
            1. Compute the total decoded length by processing each character.
            2. Traverse the string in reverse. For digits, divide the length.
               For letters, check if k mod length is zero (target found).
            3. Return the character when k becomes zero and it is a letter.

        Complexity:
            Time: O(n) where n is the length of the encoded string.
            Space: O(1)
        """
        decoded_length = 0
        for char in s:
            if char.isdigit():
                decoded_length *= int(char)
            else:
                decoded_length += 1
        for char in reversed(s):
            k %= decoded_length
            if k == 0 and char.isalpha():
                return char
            if char.isdigit():
                decoded_length //= int(char)
            else:
                decoded_length -= 1
