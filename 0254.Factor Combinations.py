class Solution:
    def getFactors(self, n: int) -> list[list[int]]:
        """Backtracking to find all unique factor combinations.

        Intuition:
            Recursively divide n by factors starting from the smallest,
            collecting valid combinations. Each factor must be >= the
            previous to avoid duplicates.

        Approach:
            Use DFS with backtracking. At each step, try dividing n by
            factors starting from the current minimum. When a valid path
            exists (non-empty), add the remaining quotient to form a
            complete combination.

        Complexity:
            Time: O(n^(1/2) * log n) for exploring factor combinations
            Space: O(log n) for recursion depth
        """

        def dfs(remainder: int, min_factor: int) -> None:
            if current_factors:
                results.append(current_factors + [remainder])
            factor = min_factor
            while factor * factor <= remainder:
                if remainder % factor == 0:
                    current_factors.append(factor)
                    dfs(remainder // factor, factor)
                    current_factors.pop()
                factor += 1

        current_factors: list[int] = []
        results: list[list[int]] = []
        dfs(n, 2)
        return results
