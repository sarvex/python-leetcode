class Solution:
    def numberOfArithmeticSlices(self, nums: list[int]) -> int:
        """Dynamic programming counting arithmetic slices with running sum.

        Intuition:
            An arithmetic slice requires at least 3 elements with constant difference.
            If nums[i] - nums[i-1] == nums[i-1] - nums[i-2], then every arithmetic
            slice ending at i-1 can be extended by one element to end at i.

        Approach:
            1. Initialize a dp array tracking arithmetic slices ending at each index.
            2. Iterate from index 2; if the difference between consecutive elements
               is constant, set dp[i] = dp[i-1] + 1.
            3. Accumulate dp[i] into total count and return.

        Complexity:
            Time: O(n), where n is the length of nums.
            Space: O(n) for the dp array.
        """

        def solve(nums: list[int]) -> int:
            length = len(nums)
            if length < 3:
                return 0

            dp = [0] * length
            count = 0

            for i in range(2, length):
                if nums[i] - nums[i - 1] == nums[i - 1] - nums[i - 2]:
                    dp[i] = dp[i - 1] + 1
                count += dp[i]

            return count

        return solve(nums)
