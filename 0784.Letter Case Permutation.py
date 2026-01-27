class Solution:
    def letterCasePermutation(self, s: str) -> list[str]:
        """DFS backtracking toggling letter case at each position.

        Intuition:
            At each character position, we can keep the original or toggle the
            case if it's a letter. This forms a binary decision tree that we
            explore with DFS.

        Approach:
            1. Convert string to a mutable list
            2. DFS from index 0: always recurse with current character
            3. If the character is alphabetic, toggle case (XOR with 32) and
               recurse again
            4. At the end of the string, append the current permutation

        Complexity:
            Time: O(2^l * n) where l is number of letters and n is string length
            Space: O(2^l * n) for storing all permutations
        """

        def dfs(index: int) -> None:
            if index >= len(s):
                results.append("".join(chars))
                return
            dfs(index + 1)
            if chars[index].isalpha():
                chars[index] = chr(ord(chars[index]) ^ 32)
                dfs(index + 1)

        chars = list(s)
        results: list[str] = []
        dfs(0)
        return results
