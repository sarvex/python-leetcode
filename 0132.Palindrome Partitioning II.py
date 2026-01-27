class Solution:
    def minCut(self, s: str) -> int:
        """Dynamic Programming with Palindrome Precomputation Approach

        Intuition:
            To minimize cuts, we need to know which substrings are palindromes and
            use DP to find the minimum number of cuts. If s[j..i] is a palindrome,
            we can transition from the optimal solution at j-1.

        Approach:
            Precompute a palindrome lookup table. Then use a 1D DP array where
            min_cuts[i] represents the minimum cuts for s[0..i]. For each position,
            check all possible palindromic suffixes and take the minimum.

        Complexity:
            Time: O(n^2) for both palindrome table and DP
            Space: O(n^2) for the palindrome table
        """
        length = len(s)
        is_palindrome = [[True] * length for _ in range(length)]
        for i in range(length - 1, -1, -1):
            for j in range(i + 1, length):
                is_palindrome[i][j] = s[i] == s[j] and is_palindrome[i + 1][j - 1]
        min_cuts = list(range(length))
        for i in range(1, length):
            for j in range(i + 1):
                if is_palindrome[j][i]:
                    min_cuts[i] = min(min_cuts[i], 1 + min_cuts[j - 1] if j else 0)
        return min_cuts[-1]
