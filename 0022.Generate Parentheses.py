from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """Generate all valid combinations of n pairs of parentheses.

        Intuition: Use backtracking to generate all possible combinations, ensuring
        that we only add valid combinations by tracking the count of open and closed
        parentheses.

        Approach: Use depth-first search with backtracking to explore all valid
        combinations. We maintain counts of open and closed parentheses, and only
        add a parenthesis if it maintains validity (open count <= n and closed count <= open count).

        Complexity:
            Time: O(4^n / sqrt(n)) - Catalan number bound for valid combinations
            Space: O(n) - Maximum recursion depth is 2n (for the call stack)
        """
        def dfs(open_count: int, close_count: int, current: str) -> None:
            # Base case: if we've used all parentheses, add to result
            if open_count == n and close_count == n:
                result.append(current)
                return

            # Add an open parenthesis if we haven't used all n
            if open_count < n:
                dfs(open_count + 1, close_count, current + '(')

            # Add a closing parenthesis if it's valid (close_count < open_count)
            if close_count < open_count:
                dfs(open_count, close_count + 1, current + ')')

        result: List[str] = []
        dfs(0, 0, '')
        return result
