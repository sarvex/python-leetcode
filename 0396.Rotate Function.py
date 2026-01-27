class Solution:
    def maxRotateFunction(self, nums: list[int]) -> int:
        """Compute maximum rotation function value using incremental update.

        Intuition:
            F(k) can be derived from F(k-1) by adding the total sum and
            subtracting n times the element that wraps around. This avoids
            recomputing from scratch each time.

        Approach:
            1. Compute F(0) = sum(i * nums[i]).
            2. For each subsequent rotation, update using the relation:
               F(k) = F(k-1) + total_sum - n * nums[n-k].
            3. Track and return the maximum value seen.

        Complexity:
            Time: O(n)
            Space: O(1)
        """
        current_value = sum(i * value for i, value in enumerate(nums))
        length, total_sum = len(nums), sum(nums)
        max_value = current_value
        for i in range(1, length):
            current_value = current_value + total_sum - length * nums[length - i]
            max_value = max(max_value, current_value)
        return max_value
