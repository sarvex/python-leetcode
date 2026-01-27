from heapq import heapify, heappop, heappush


class Solution:
    def kthSmallestPrimeFraction(self, arr: list[int], k: int) -> list[int]:
        """Min-heap of fractions with lazy expansion of numerator candidates.

        Intuition:
            For a sorted array of primes, fractions arr[i]/arr[j] with i < j form
            a matrix where each row is sorted. We use a min-heap to efficiently
            find the k-th smallest by expanding one row at a time.

        Approach:
            1. Initialize heap with fractions 1/arr[j] for all denominators
            2. Pop the smallest fraction k-1 times
            3. After each pop, push the next fraction in that row (increment numerator index)
            4. The k-th popped element is the answer

        Complexity:
            Time: O(k * log n) where n is the array length
            Space: O(n) for the heap
        """
        heap = [(1 / arr[j + 1], 0, j + 1) for j in range(len(arr) - 1)]
        heapify(heap)
        for _ in range(k - 1):
            _, numer_idx, denom_idx = heappop(heap)
            if numer_idx + 1 < denom_idx:
                heappush(
                    heap,
                    (arr[numer_idx + 1] / arr[denom_idx], numer_idx + 1, denom_idx),
                )
        return [arr[heap[0][1]], arr[heap[0][2]]]
