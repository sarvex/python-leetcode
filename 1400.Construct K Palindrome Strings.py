from collections import Counter


class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        """Determine if s can be rearranged into exactly k palindromes.

        Intuition:
            A palindrome can have at most one character with odd frequency.
            So we need at least as many palindromes as odd-frequency characters.

        Approach:
            Count character frequencies. The number of characters with odd
            frequency is the minimum number of palindromes needed. Also,
            we cannot have more palindromes than the string length.

        Complexity:
            Time: O(n) for counting characters
            Space: O(1) since alphabet is fixed size
        """
        if len(s) < k:
            return False
        frequency = Counter(s)
        odd_count = sum(count & 1 for count in frequency.values())
        return odd_count <= k
