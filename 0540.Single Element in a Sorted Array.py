class Solution:
    def singleNonDuplicate(self, nums: list[int]) -> int:
        """Binary search using index parity to find the single element.

        Intuition:
            In a sorted array where every element appears twice except one,
            the pairs are disrupted at the single element. Binary search
            can identify the disruption point using XOR with 1.

        Approach:
            Binary search on the array. At each midpoint, XOR the index with 1
            to find its expected pair. If the pair doesn't match, the single
            element is on the left; otherwise, on the right.

        Complexity:
            Time: O(log n)
            Space: O(1)
        """
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) >> 1
            if nums[mid] != nums[mid ^ 1]:
                right = mid
            else:
                left = mid + 1
        return nums[left]
