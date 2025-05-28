from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """Backtracking with DFS to find all unique combinations that sum to target
        
        Intuition:
        Use backtracking to explore all possible combinations, allowing reuse of elements.
        Sorting the candidates first allows for early termination when sum exceeds target.
        
        Approach:
        1. Sort the candidates to enable pruning
        2. Use DFS to explore combinations, starting from each position
        3. For each position, we can either include the current number multiple times or move to next
        4. When current sum equals target, add the combination to results
        5. When current sum exceeds target, backtrack
        
        Complexity:
        Time: O(N^(T/M)) where N is length of candidates, T is target, M is minimum value in candidates
        Space: O(T/M) for recursion stack depth
        """
        def dfs(i: int, remaining: int) -> None:
            if remaining == 0:
                # Found a valid combination
                result.append(current_combination[:])
                return
                
            if i >= len(candidates) or remaining < candidates[i]:
                # Base case: out of bounds or remaining is too small
                return
                
            # Include current candidate multiple times
            current_combination.append(candidates[i])
            dfs(i, remaining - candidates[i])
            current_combination.pop()
            
            # Skip current candidate and move to next
            dfs(i + 1, remaining)
        
        candidates.sort()
        current_combination: List[int] = []
        result: List[List[int]] = []
        dfs(0, target)
        return result
