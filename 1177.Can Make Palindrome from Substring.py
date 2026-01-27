class Solution:
    def canMakePaliQueries(self, s: str, queries: list[list[int]]) -> list[bool]:
        """Check if substrings can form palindromes with at most k replacements.

        Intuition:
            A string can be rearranged into a palindrome if at most one character
            has an odd frequency. Each replacement fixes two odd-count characters.

        Approach:
            Build a prefix frequency array for all 26 letters. For each query,
            count characters with odd frequency in the substring and check if
            half that count is within the allowed replacements.

        Complexity:
            Time: O(26 * (n + q))
            Space: O(26 * n)
        """
        n = len(s)
        prefix_counts = [[0] * 26 for _ in range(n + 1)]
        for i, ch in enumerate(s, 1):
            prefix_counts[i] = prefix_counts[i - 1][:]
            prefix_counts[i][ord(ch) - ord("a")] += 1

        result: list[bool] = []
        for left, right, max_replacements in queries:
            odd_count = sum(
                (prefix_counts[right + 1][j] - prefix_counts[left][j]) & 1
                for j in range(26)
            )
            result.append(odd_count // 2 <= max_replacements)
        return result
