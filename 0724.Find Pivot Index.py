from typing import List

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        """Find the leftmost pivot index in the array.

        Intuition:
        Use prefix sums to efficiently check if the sum of elements to the left equals
        the sum of elements to the right of each potential pivot.

        Approach:
        1. Calculate the total sum of the array
        2. Iterate through each element, tracking left sum and calculating right sum
        3. At each position, check if left sum equals right sum
        4. Return the first index where this condition is met

        Complexity:
        Time: O(n) where n is the length of the array (one pass to calculate sum, one pass to find pivot)
        Space: O(1) as we only use constant extra space
        """
        left = 0
        right = sum(nums)

        for i, num in enumerate(nums):
            # Right sum is total sum minus current element and left sum
            right -= num

            if left == right:
                return i

            left += num
        return -1
