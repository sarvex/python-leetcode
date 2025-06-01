from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """Two-pointer approach to find all unique triplets that sum to zero.

        Intuition:
        Sort the array first to easily skip duplicates and use two pointers to find
        pairs that sum to the negative of each element.

        Approach:
        1. Sort the array to handle duplicates efficiently
        2. Iterate through each element as a potential first number
        3. For each first number, use two pointers to find pairs that sum to its negative
        4. Skip duplicate values to avoid duplicate triplets
        5. Use early termination when first number is positive (impossible to sum to zero)

        Complexity:
        Time: O(n²) where n is the length of the input array
        Space: O(1) excluding the output array (or O(n) if sorting is not in-place)
        """
        nums.sort()
        n = len(nums)
        result = []

        for i in range(n - 2):
            # Early termination: if first number > 0, impossible to sum to zero
            if nums[i] > 0:
                break

            # Skip duplicates for first position
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Two-pointer technique to find pairs
            left, right = i + 1, n - 1
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]

                if current_sum < 0:
                    left += 1
                elif current_sum > 0:
                    right -= 1
                else:
                    # Found a triplet
                    result.append([nums[i], nums[left], nums[right]])

                    # Move both pointers and skip duplicates
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

        return result
