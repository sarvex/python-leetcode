from typing import List


class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        """Divide array into subarrays with max difference constraint

        Intuition:
        If we sort the array, elements close to each other in the sorted order will have
        minimal differences. By grouping consecutive elements, we can minimize the maximum
        difference within each group.

        Approach:
        1. Sort the array to bring similar elements together
        2. Divide the sorted array into groups of 3 elements each
        3. For each group, check if the difference between max and min is at most k
        4. If any group violates this condition, return an empty array

        Complexity:
        Time: O(n log n) due to sorting
        Space: O(n) for the result array
        """
        nums.sort()
        result = []
        n = len(nums)

        for i in range(0, n, 3):
            group = nums[i:i+3]
            if group[2] - group[0] > k:
                return []
            result.append(group)

        return result
