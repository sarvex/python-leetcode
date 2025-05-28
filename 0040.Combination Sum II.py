from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        Backtracking with sorting and skipping duplicates
        
        Intuition:
        When finding combinations that sum to target, we need to avoid duplicate combinations.
        By sorting the candidates first, we can easily skip duplicates during our search.
        
        Approach:
        1. Sort the candidates to handle duplicates efficiently
        2. Use backtracking (DFS) to explore all possible combinations
        3. For each position, skip consecutive duplicates to avoid duplicate combinations
        4. When the sum equals target, add the current combination to the result
        5. Use early termination when sum exceeds target or we've reached the end of candidates
        
        Complexity:
        Time: O(2^n), where n is the length of candidates (worst case scenario)
        Space: O(target), for the recursion stack and to store the current combination
        """
        def dfs(start: int, remaining: int, path: List[int]) -> None:
            """Explore all valid combinations starting from index 'start' with 'remaining' sum."""
            if remaining == 0:
                # Found a valid combination
                result.append(path[:])
                return
                
            if start >= len(candidates) or remaining < candidates[start]:
                # Early termination: out of bounds or remaining sum too small
                return
                
            for i in range(start, len(candidates)):
                # Skip duplicates at the same level of recursion
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                    
                # Include current candidate
                path.append(candidates[i])
                # Move to next position (can't reuse same element)
                dfs(i + 1, remaining - candidates[i], path)
                # Backtrack
                path.pop()

        # Sort candidates to handle duplicates
        candidates.sort()
        result: List[List[int]] = []
        dfs(0, target, [])
        return result
