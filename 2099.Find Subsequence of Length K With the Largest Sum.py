from typing import List

class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        """Find subsequence of length k with the largest sum while maintaining relative order.

        Intuition:
        To maximize the sum, we need to select the k largest elements from the array.
        However, we must maintain their original relative order in the final result.

        Approach:
        1. Create indices for all elements and sort them by their values in descending order
        2. Take the k indices with the largest values
        3. Sort these k indices to maintain the original order
        4. Return the elements at these indices

        Complexity:
        Time: O(n log n) where n is the length of nums due to sorting operations
        Space: O(n) for storing indices and the result
        """
        # Get indices of k largest elements (sort by negative value to get descending order)
        largest_indices = sorted(range(len(nums)), key=lambda i: -nums[i])[:k]

        # Sort indices to maintain original relative order
        return [nums[i] for i in sorted(largest_indices)]
