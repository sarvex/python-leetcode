from heapq import heapify, heappop, heappush


class Solution:
    def kSmallestPairs(
        self, nums1: list[int], nums2: list[int], k: int
    ) -> list[list[int]]:
        """Find k pairs with smallest sums using a min-heap.

        Intuition:
            Since both arrays are sorted, the smallest pair sum starts at
            (nums1[0], nums2[0]). Use a heap to efficiently explore the
            next smallest pairs by incrementing the index in nums2.

        Approach:
            Initialize a min-heap with pairs (nums1[i] + nums2[0], i, 0) for
            the first k elements of nums1. Pop the smallest sum, record the
            pair, and push the next pair with the incremented nums2 index.
            Continue until k pairs are collected or the heap is empty.

        Complexity:
            Time: O(k log k)
            Space: O(k)
        """
        heap = [[val + nums2[0], i, 0] for i, val in enumerate(nums1[:k])]
        heapify(heap)
        result: list[list[int]] = []
        while heap and k > 0:
            _, idx1, idx2 = heappop(heap)
            result.append([nums1[idx1], nums2[idx2]])
            k -= 1
            if idx2 + 1 < len(nums2):
                heappush(heap, [nums1[idx1] + nums2[idx2 + 1], idx1, idx2 + 1])
        return result
