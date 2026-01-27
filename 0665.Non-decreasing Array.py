from itertools import pairwise


class Solution:
    def checkPossibility(self, nums: list[int]) -> bool:
        """Check if array can become non-decreasing by modifying at most one element.

        Intuition:
        Find the first violation where nums[i] > nums[i+1]. Try fixing it by
        either lowering nums[i] or raising nums[i+1], then check if the result
        is sorted.

        Approach:
        1. Scan for the first pair where nums[i] > nums[i+1].
        2. Try setting nums[i] = nums[i+1] and check if sorted.
        3. If not, try setting nums[i+1] = nums[i] and check if sorted.
        4. If no violation found, array is already non-decreasing.

        Complexity:
        Time: O(n)
        Space: O(1)
        """

        def is_sorted(arr: list[int]) -> bool:
            return all(a <= b for a, b in pairwise(arr))

        length = len(nums)
        for i in range(length - 1):
            prev, curr = nums[i], nums[i + 1]
            if prev > curr:
                nums[i] = curr
                if is_sorted(nums):
                    return True
                nums[i] = nums[i + 1] = prev
                return is_sorted(nums)
        return True
