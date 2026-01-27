class Solution:
    def removePalindromeSub(self, s: str) -> int:
        """Remove palindromic subsequences to empty the string (only 'a' and 'b').

        Intuition:
            Since the string contains only 'a' and 'b', at most 2 moves suffice:
            remove all 'a's then all 'b's. If already a palindrome, 1 move.

        Approach:
            Check if the string is a palindrome. If yes, return 1; otherwise 2.

        Complexity:
            Time: O(n)
            Space: O(n) for the reversed string comparison
        """
        return 1 if s[::-1] == s else 2
