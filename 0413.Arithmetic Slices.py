from typing import List

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        """
        Approach:
        1. Initialize a dp array to keep track of arithmetic slices ending at each index.
        2. Iterate through the array starting from index 2.
           - If the difference between consecutive elements is constant,
             increment the count for the current index based on previous counts.
        3. Return the total count of arithmetic slices.

        Complexity:
        Time: O(n), where n is the length of nums.
        Space: O(1), as we only use a constant amount of extra space.
        """
        def solve(nums):
            n = len(nums)
            if n < 3:
                return 0

            dp = [0] * n
            count = 0

            for i in range(2, n):
                if nums[i] - nums[i-1] == nums[i-1] - nums[i-2]:
                    dp[i] = dp[i-1] + 1
                count += dp[i]

            return count
        
        return solve(nums)
