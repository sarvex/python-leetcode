from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        Two-pointer approach with constant space complexity

        Intuition:
        Allow each element to appear at most twice. We can use a counter to track
        how many elements we've kept so far and only add a new element if it's different
        from the element two positions back in our result array.

        Approach:
        1. Use a pointer k to track the position where the next element should be placed
        2. Iterate through the array and place elements at position k if:
           - We have fewer than 2 elements (k < 2), or
           - The current element is different from the element at k-2
        3. Return k as the new length of the modified array

        Complexity:
        Time: O(n) where n is the length of the input array
        Space: O(1) as we modify the array in-place
        """
        k = 0
        for num in nums:
            if k < 2 or num != nums[k - 2]:
                nums[k] = num
                k += 1
        return k
