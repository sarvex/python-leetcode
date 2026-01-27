class Solution:
    def rob(self, nums: list[int]) -> int:
        """Dynamic programming on circular array by splitting into two linear cases.

        Intuition:
            Since houses form a circle, the first and last house cannot both be
            robbed. Split the problem into two linear house robber subproblems.

        Approach:
            1. If only one house, return its value.
            2. Solve linear house robber for nums[1:] and nums[:-1].
            3. Return the maximum of both results.

        Complexity:
            Time: O(n)
            Space: O(1)
        """

        def rob_linear(houses: list[int]) -> int:
            skip, take = 0, 0
            for amount in houses:
                skip, take = max(skip, take), skip + amount
            return max(skip, take)

        if len(nums) == 1:
            return nums[0]
        return max(rob_linear(nums[1:]), rob_linear(nums[:-1]))
