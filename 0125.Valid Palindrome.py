class Solution:
    def isPalindrome(self, s: str) -> bool:
        """Two-pointer approach to validate palindromes

        Intuition:
        A palindrome reads the same forward and backward, so we can use two pointers
        starting from both ends of the string and move inward, comparing characters.

        Approach:
        1. Initialize two pointers at the start and end of the string
        2. Skip non-alphanumeric characters
        3. Compare characters (case-insensitive)
        4. If all comparisons match, it's a palindrome

        Complexity:
        Time: O(n) where n is the length of the string
        Space: O(1) as we only use two pointers regardless of input size
        """
        left, right = 0, len(s) - 1

        while left < right:
            if not s[left].isalnum():
                left += 1
            elif not s[right].isalnum():
                right -= 1
            elif s[left].lower() != s[right].lower():
                return False
            else:
                left += 1
                right -= 1

        return True
