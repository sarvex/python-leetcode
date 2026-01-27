from heapq import heapify, heappop, heappush


class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        """Max-heap approach for sliding window maximum.

        Intuition:
            A max-heap can track the largest element efficiently. We store
            negated values with indices and lazily remove out-of-window elements.

        Approach:
            Initialize a max-heap with the first k-1 elements. For each new
            element, push it onto the heap, then pop elements whose indices
            are outside the current window. The heap top is the window maximum.

        Complexity:
            Time: O(n log n)
            Space: O(n)
        """
        heap = [(-value, index) for index, value in enumerate(nums[: k - 1])]
        heapify(heap)
        result = []
        for i in range(k - 1, len(nums)):
            heappush(heap, (-nums[i], i))
            while heap[0][1] <= i - k:
                heappop(heap)
            result.append(-heap[0][0])
        return result
