from typing import List

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        """
        Backtracking with pruning to find all unique combinations of k numbers that sum to n.

        Intuition:
        Use backtracking to explore combinations of numbers 1-9, with each number used at most once.

        Approach:
        1. Use DFS with backtracking to build combinations
        2. For each position, decide whether to include the current number or skip it
        3. Prune branches where:
           - We've collected k numbers
           - Current sum exceeds target
           - Current number exceeds 9
        4. Add valid combinations to the result when we have k numbers that sum to n

        Complexity:
        Time: O(C(9,k) * k) where C(9,k) is the binomial coefficient (number of ways to choose k from 9)
        Space: O(k) for recursion stack and current combination
        """
        def dfs(i: int, remaining: int, path: List[int]) -> None:
            # Base case: found a valid combination
            if remaining == 0 and len(path) == k:
                result.append(path[:])
                return

            # Pruning conditions
            if i > 9 or len(path) >= k or remaining < 0:
                return

            # Take the current number
            path.append(i)
            dfs(i + 1, remaining - i, path)

            # Skip the current number (backtrack)
            path.pop()
            dfs(i + 1, remaining, path)

        result = []
        dfs(1, n, [])
        return result
