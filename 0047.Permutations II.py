from typing import List

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        """Generate all possible unique permutations of the input array.

        Intuition: Use backtracking with sorting to handle duplicates efficiently.

        Approach:
        1. Sort the array to group duplicates together
        2. Use DFS with a visited array to track used elements
        3. Skip duplicates by checking if the current number equals the previous number
           and the previous number is not used in the current permutation

        Complexity:
        Time: O(n * n!), where n is the length of nums
        Space: O(n), for recursion stack and temporary arrays
        """
        def dfs(i: int) -> None:
            # Base case: if we've filled all positions, add the permutation to results
            if i == n:
                ans.append(t[:])
                return

            for j in range(n):
                # Skip if element is used or it's a duplicate in an invalid position
                if vis[j] or (j > 0 and nums[j] == nums[j - 1] and not vis[j - 1]):
                    continue

                # Use the current element at position i
                t[i] = nums[j]
                vis[j] = True
                dfs(i + 1)
                vis[j] = False  # Backtrack

        n = len(nums)
        nums.sort()  # Sort to handle duplicates
        ans = []
        t = [0] * n  # Temporary array to build permutations
        vis = [False] * n  # Track visited elements
        dfs(0)
        return ans
