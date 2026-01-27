class Solution:
    def maxWidthRamp(self, nums: list[int]) -> int:
        """Monotonic stack with reverse scan for maximum width ramp.

        Intuition:
            Build a decreasing stack of indices from left to right (potential ramp starts).
            Then scan from right to left, popping stack entries that form valid ramps
            to maximize width.

        Approach:
            1. Build a monotonic decreasing stack of values (by index).
            2. Traverse from right to left; for each position, pop stack entries
               where nums[stack_top] <= nums[current].
            3. Track the maximum ramp width (current_index - stack_top_index).

        Complexity:
            Time: O(n) — each element pushed and popped at most once
            Space: O(n) — stack storage
        """
        stack = []
        for index, value in enumerate(nums):
            if not stack or nums[stack[-1]] > value:
                stack.append(index)
        max_width = 0
        for index in range(len(nums) - 1, -1, -1):
            while stack and nums[stack[-1]] <= nums[index]:
                max_width = max(max_width, index - stack.pop())
            if not stack:
                break
        return max_width
