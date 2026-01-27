class Solution:
    def findUnsortedSubarray(self, nums: list[int]) -> int:
        """Find shortest subarray that when sorted makes the whole array sorted.

        Intuition:
            Compare the original array with its sorted version. The unsorted
            subarray spans from the first mismatch to the last mismatch.

        Approach:
            1. Create a sorted copy of the array.
            2. Move left pointer forward while elements match the sorted array.
            3. Move right pointer backward while elements match the sorted array.
            4. The distance between pointers gives the subarray length.

        Complexity:
            Time: O(n log n)
            Space: O(n)
        """
        sorted_nums = sorted(nums)
        left, right = 0, len(nums) - 1
        while left <= right and nums[left] == sorted_nums[left]:
            left += 1
        while left <= right and nums[right] == sorted_nums[right]:
            right -= 1
        return right - left + 1
