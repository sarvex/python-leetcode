class Solution:
    def decompressRLElist(self, nums: list[int]) -> list[int]:
        """Decompress a run-length encoded list.

        Intuition:
            Pairs of (frequency, value) encode the list, so iterate by steps of 2.

        Approach:
            For each pair at indices (i-1, i), extend the result with nums[i]
            repeated nums[i-1] times.

        Complexity:
            Time: O(n + total_elements) where n is length of nums
            Space: O(total_elements) for the decompressed result
        """
        result: list[int] = []
        for i in range(1, len(nums), 2):
            result.extend([nums[i]] * nums[i - 1])
        return result
