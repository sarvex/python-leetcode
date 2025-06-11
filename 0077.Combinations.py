from typing import List
from itertools import combinations

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        """
        Backtracking with decision tree approach to generate all combinations.

        Intuition:
        For each number from 1 to n, we have two choices: either include it in the
        current combination or exclude it. This forms a binary decision tree.

        Approach:
        Use backtracking to explore all possible combinations. At each step:
        1. If we have k elements, add the current combination to our result
        2. If we've gone beyond n, return as there are no more elements to consider
        3. Otherwise, make two recursive calls:
           - Include the current number and move to the next
           - Skip the current number and move to the next

        Complexity:
        Time: O(C(n,k)) - We generate exactly C(n,k) combinations
        Space: O(k) - O(k) for recursion stack and storing each combination
        """
        def dfs(i: int) -> None:
            # Base case: found a valid combination
            if len(current) == k:
                result.append(current[:])
                return

            # Optimization: early pruning if remaining elements are insufficient
            if i > n or len(current) + (n - i + 1) < k:
                return

            # Include current element
            current.append(i)
            dfs(i + 1)

            # Exclude current element (backtrack)
            current.pop()
            dfs(i + 1)

        result: List[List[int]] = []
        current: List[int] = []
        dfs(1)
        return result

    def combine_itertools(self, n: int, k: int) -> List[List[int]]:
        """
        Built-in solution using Python's itertools.combinations.

        Intuition:
        Python's standard library provides an efficient implementation for generating
        combinations that we can leverage directly.

        Approach:
        Use itertools.combinations to generate all k-length combinations from range(1, n+1).

        Complexity:
        Time: O(C(n,k)) - We generate exactly C(n,k) combinations
        Space: O(C(n,k)) - To store all combinations
        """
        return list(combinations(range(1, n + 1), k))
