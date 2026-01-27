class Solution:
    def shortestPalindrome(self, s: str) -> str:
        """Rolling hash to find the longest palindrome prefix.

        Intuition:
            Find the longest palindromic prefix of s, then prepend the reverse
            of the remaining suffix to form the shortest palindrome.

        Approach:
            1. Compute forward and reverse rolling hashes simultaneously.
            2. When hashes match, record the position as a potential palindrome end.
            3. Reverse the suffix after the longest palindrome prefix and prepend it.

        Complexity:
            Time: O(n)
            Space: O(n) for the output string
        """
        base = 131
        mod = 10**9 + 7
        length = len(s)
        prefix_hash = suffix_hash = 0
        multiplier = 1
        palindrome_end = 0
        for idx, char in enumerate(s):
            char_val = ord(char) - ord("a") + 1
            prefix_hash = (prefix_hash * base + char_val) % mod
            suffix_hash = (suffix_hash + char_val * multiplier) % mod
            multiplier = (multiplier * base) % mod
            if prefix_hash == suffix_hash:
                palindrome_end = idx + 1
        return s if palindrome_end == length else s[palindrome_end:][::-1] + s
