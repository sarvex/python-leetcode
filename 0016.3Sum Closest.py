from typing import List
from math import inf


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        """Find the sum of three integers in nums that is closest to the target.

        Intuition: Sort the array and use two pointers to find the closest sum.

        Approach:
        1. Sort the array to enable the two-pointer technique
        2. Iterate through each element as a potential first number
        3. Use two pointers to find the other two numbers
        4. Track the sum that is closest to the target
        5. Adjust pointers based on comparison with target

        Complexity:
        Time: O(n²) where n is the length of nums (sorting is O(n log n) and nested loop is O(n²))
        Space: O(1) or O(log n) depending on the sorting algorithm's implementation
        """
        nums.sort()
        n = len(nums)
        ans = inf

        for i, v in enumerate(nums):
            j, k = i + 1, n - 1
            while j < k:
                t = v + nums[j] + nums[k]
                if t == target:
                    return t
                if abs(t - target) < abs(ans - target):
                    ans = t
                if t > target:
                    k -= 1
                else:
                    j += 1
        return ans
