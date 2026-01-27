class Solution:
    def smallestRangeI(self, nums: list[int], k: int) -> int:
        """Greedy approach using max and min difference.

        Intuition:
            The minimum possible range after adding values in [-k, k] to each
            element is determined by whether the gap between max and min can
            be closed by adjusting both ends by k.

        Approach:
            1. Find the maximum and minimum of the array.
            2. The best we can do is reduce the gap by 2*k.
            3. Return max(0, max_val - min_val - 2*k).

        Complexity:
            Time: O(n)
            Space: O(1)
        """
        max_val, min_val = max(nums), min(nums)
        return max(0, max_val - min_val - k * 2)
