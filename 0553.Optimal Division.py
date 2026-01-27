class Solution:
    def optimalDivision(self, nums: list[int]) -> str:
        """Maximize division result by parenthesizing the denominator.

        Intuition:
            To maximize a/b/c/d/..., we want to minimize the denominator.
            Dividing b by everything after it (c/d/...) minimizes the overall
            denominator, so we parenthesize nums[1:].

        Approach:
            1. If only one number, return it as a string.
            2. If two numbers, return a/b.
            3. Otherwise, return a/(b/c/d/...) to maximize the result.

        Complexity:
            Time: O(n)
            Space: O(n)
        """
        length = len(nums)
        if length == 1:
            return str(nums[0])
        if length == 2:
            return f"{nums[0]}/{nums[1]}"
        return f"{nums[0]}/({'/'.join(map(str, nums[1:]))})"
