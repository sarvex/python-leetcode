from functools import cache


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        """Dynamic programming with memoization for wildcard pattern matching.
        
        Intuition:
            The problem can be solved using recursive pattern matching with three cases:
            1. When we encounter '*', we have multiple choices
            2. When we encounter '?', it matches any single character
            3. Otherwise, characters must match exactly
        
        Approach:
            Use top-down dynamic programming with memoization to avoid redundant calculations.
            For each position (i, j) in strings s and p, we determine if the substrings
            s[i:] and p[j:] match. We handle special cases for '*' which can match
            zero or more characters.
        
        Complexity:
            Time: O(m*n) where m is length of s and n is length of p
            Space: O(m*n) for memoization cache
        """
        @cache
        def dfs(i: int, j: int) -> bool:
            # Base cases
            if i >= len(s):
                # If s is exhausted, p must be exhausted or only contain '*'
                return j >= len(p) or all(p[k] == '*' for k in range(j, len(p)))
            if j >= len(p):
                # If p is exhausted but s is not, no match
                return False
            
            # Handle wildcard '*'
            if p[j] == '*':
                # Three options:
                # 1. '*' matches current char and we continue matching rest of s with same pattern
                # 2. '*' matches current char and we move to next pattern char
                # 3. '*' matches empty string, we just move to next pattern char
                return dfs(i + 1, j) or dfs(i + 1, j + 1) or dfs(i, j + 1)
            
            # Handle single character match ('?' or exact match)
            if p[j] == '?' or s[i] == p[j]:
                return dfs(i + 1, j + 1)
            
            # No match
            return False

        # Optimize pattern by removing consecutive '*'
        optimized_p = []
        for char in p:
            if not optimized_p or char != '*' or optimized_p[-1] != '*':
                optimized_p.append(char)
        
        return dfs(0, 0)
