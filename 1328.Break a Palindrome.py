class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        """Break a palindrome by replacing one character to make it lexicographically smallest.

        Intuition:
            Replace the first non-'a' character in the first half with 'a'.
            If all characters in the first half are 'a', change the last character to 'b'.

        Approach:
            Scan the first half for a character other than 'a' and replace it.
            If none found, replace the last character with 'b'. Single character
            palindromes cannot be broken.

        Complexity:
            Time: O(n)
            Space: O(n) for the character list
        """
        length = len(palindrome)
        if length == 1:
            return ""
        chars = list(palindrome)
        index = 0
        while index < length // 2 and chars[index] == "a":
            index += 1
        if index == length // 2:
            chars[-1] = "b"
        else:
            chars[index] = "a"
        return "".join(chars)
