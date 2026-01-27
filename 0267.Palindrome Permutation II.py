from collections import Counter


class Solution:
    def generatePalindromes(self, s: str) -> list[str]:
        """Backtracking to generate all palindrome permutations from character counts.

        Intuition:
            Only need to generate the first half of the palindrome since the second
            half is a mirror. An odd-count character goes in the middle.

        Approach:
            1. Count character frequencies. If more than one has an odd count, return empty.
            2. Identify the middle character (if any) and reduce its count by 1.
            3. Use DFS backtracking to build palindromes by placing matching pairs
               on both sides simultaneously.
            4. Collect all valid palindromes.

        Complexity:
            Time: O((n/2)!) in the worst case for generating permutations
            Space: O(n) for the recursion stack and result storage
        """

        def dfs(current: str) -> None:
            if len(current) == len(s):
                result.append(current)
                return
            for char, count in char_counts.items():
                if count > 1:
                    char_counts[char] -= 2
                    dfs(char + current + char)
                    char_counts[char] += 2

        char_counts = Counter(s)
        middle = ""
        for char, count in char_counts.items():
            if count & 1:
                if middle:
                    return []
                middle = char
                char_counts[char] -= 1
        result: list[str] = []
        dfs(middle)
        return result
