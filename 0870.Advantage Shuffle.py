class Solution:
    def advantageCount(self, nums1: list[int], nums2: list[int]) -> list[int]:
        """Greedy assignment using sorted order to maximize advantage.

        Intuition:
            Sort nums1 and greedily assign the smallest element that beats
            each element in nums2. If no element can beat it, assign the
            smallest remaining (waste the weakest).

        Approach:
            1. Sort nums1 in ascending order.
            2. Sort nums2 by value while keeping original indices.
            3. Use two pointers on sorted nums2: one at the weakest, one at
               the strongest. For each value in sorted nums1, assign it to
               beat the weakest if possible, otherwise waste it on the strongest.

        Complexity:
            Time: O(n log n)
            Space: O(n)
        """
        nums1.sort()
        sorted_nums2 = sorted((value, index) for index, value in enumerate(nums2))
        length = len(nums2)
        result = [0] * length
        low, high = 0, length - 1
        for value in nums1:
            if value <= sorted_nums2[low][0]:
                result[sorted_nums2[high][1]] = value
                high -= 1
            else:
                result[sorted_nums2[low][1]] = value
                low += 1
        return result
