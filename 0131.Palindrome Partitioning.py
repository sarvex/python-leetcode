class Solution:
    def partition(self, s: str) -> list[list[str]]:
        """Backtracking with Precomputed Palindrome Table Approach

        Intuition:
            We need all possible ways to partition a string into palindromic
            substrings. Precomputing which substrings are palindromes allows
            efficient pruning during backtracking.

        Approach:
            Build a 2D boolean table where is_palindrome[i][j] indicates if
            s[i..j] is a palindrome, using dynamic programming. Then use
            backtracking to explore all valid partitions, only extending when
            the current substring is a palindrome.

        Complexity:
            Time: O(n * 2^n) for generating all partitions
            Space: O(n^2) for the palindrome table
        """

        def dfs(start: int) -> None:
            if start == length:
                result.append(current[:])
                return
            for end in range(start, length):
                if is_palindrome[start][end]:
                    current.append(s[start : end + 1])
                    dfs(end + 1)
                    current.pop()

        length = len(s)
        is_palindrome = [[True] * length for _ in range(length)]
        for i in range(length - 1, -1, -1):
            for j in range(i + 1, length):
                is_palindrome[i][j] = s[i] == s[j] and is_palindrome[i + 1][j - 1]
        result: list[list[str]] = []
        current: list[str] = []
        dfs(0)
        return result
