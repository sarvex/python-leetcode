from typing import List
from heapq import heappush, heappop

class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        """Greedy approach with min-heap for maximum subsequence score.

        Intuition:
            The score is defined as (sum of selected nums1 elements) * (minimum of selected nums2 elements).
            To maximize this product, we need to balance between high sum from nums1 and high minimum from nums2.

        Approach:
            1. Sort pairs (nums2[i], nums1[i]) by nums2 in descending order
            2. Process pairs in order, maintaining a min-heap of k nums1 values
            3. For each pair, calculate score using current nums2 value as minimum
            4. Keep track of maximum score seen

        Complexity:
            Time: O(n log n) where n is the length of nums1/nums2 (for sorting and heap operations)
            Space: O(n) for storing the sorted pairs and heap
        """
        # Sort pairs by nums2 values in descending order
        pairs = sorted(zip(nums2, nums1), reverse=True)

        # Min heap to maintain k largest nums1 values
        min_heap = []
        current_sum = 0
        max_score = 0

        for min_val, add_val in pairs:
            # Add current nums1 value to sum
            current_sum += add_val
            heappush(min_heap, add_val)

            # If we have more than k elements, remove the smallest
            if len(min_heap) > k:
                current_sum -= heappop(min_heap)

            # If we have exactly k elements, calculate score
            if len(min_heap) == k:
                max_score = max(max_score, current_sum * min_val)

        return max_score
