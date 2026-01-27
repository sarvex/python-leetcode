class Solution:
    def minIncrementForUnique(self, nums: list[int]) -> int:
        """Sort and greedily assign minimum unique values.

        Intuition:
            After sorting, each element must be at least one more than the
            previous assigned value. The difference is the number of increments needed.

        Approach:
            1. Sort the array.
            2. Track the minimum acceptable value (previous assigned + 1).
            3. For each number, assign max(current, min_acceptable).
            4. Sum up all increments needed.

        Complexity:
            Time: O(n log n) — dominated by sorting
            Space: O(1) — in-place sort, constant extra space
        """
        nums.sort()
        total_increments, next_available = 0, -1
        for num in nums:
            next_available = max(next_available + 1, num)
            total_increments += next_available - num
        return total_increments
