from collections import Counter


class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        """Count character frequencies to check if a palindrome permutation exists.

        Intuition:
            A string can form a palindrome if at most one character has an odd
            frequency count.

        Approach:
            1. Count the frequency of each character.
            2. Count how many characters have odd frequencies.
            3. Return True if fewer than 2 characters have odd counts.

        Complexity:
            Time: O(n) where n is the length of s
            Space: O(k) where k is the number of distinct characters
        """
        return sum(count & 1 for count in Counter(s).values()) < 2
