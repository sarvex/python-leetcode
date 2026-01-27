class Solution:
    def countSubstrings(self, s: str) -> int:
        """Expand around center to count all palindromic substrings.

        Intuition:
        Every palindrome has a center (single char for odd length, between chars
        for even length). Expand outward from each possible center.

        Approach:
        1. Iterate over 2n-1 possible centers (odd and even length palindromes).
        2. For each center, expand outward while characters match.
        3. Count each valid expansion as a palindromic substring.

        Complexity:
        Time: O(n^2)
        Space: O(1)
        """
        count, length = 0, len(s)
        for center in range(length * 2 - 1):
            left, right = center // 2, (center + 1) // 2
            while ~left and right < length and s[left] == s[right]:
                count += 1
                left, right = left - 1, right + 1
        return count
