from heapq import heappop, heappush, heapify
from typing import List


class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        """Minimum difference in sums after removal of elements.

        Intuition: Use priority queues to efficiently maintain the minimum sum of first n elements
        and maximum sum of last n elements, then find the minimum difference between them.

        Approach:
        1. For the first part (prefix), maintain a max heap of size n to get the n smallest elements
           - Initialize with first n elements (negated for max heap)
           - For each element in range [n, 2n), update the heap if current element is smaller
           - Calculate prefix sums for each valid split point

        2. For the second part (suffix), maintain a min heap of size n to get the n smallest elements
           - Initialize with last n elements
           - For each element in range [2n-1, n-1], update the heap if current element is larger
           - Calculate suffix sums for each valid split point

        3. Find the minimum difference between corresponding prefix and suffix sums

        Complexity:
        Time: O(n log n), where n = len(nums)/3
        Space: O(n) for storing prefix and suffix arrays and heaps
        """
        n = len(nums) // 3

        # For each range [0,n], ... [0,2n-1], find minimum n elements and store their sum
        max_heap = [-v for v in nums[:n]]  # Negate values for max heap
        heapify(max_heap)
        prefix_sums = [-sum(max_heap)]  # Sum of n smallest elements in first n positions

        for v in nums[n:2*n]:
            current_sum = prefix_sums[-1]
            # If current element is smaller than the largest element in our heap
            if -v > max_heap[0]:
                # Remove largest element from sum
                current_sum -= -heappop(max_heap)
                # Add current element to heap and sum
                heappush(max_heap, -v)
                current_sum += v
            prefix_sums.append(current_sum)

        # For each range [n,3n], ... [2n,3n], find maximum n elements and store their sum
        min_heap = nums[2*n:]  # Last n elements
        heapify(min_heap)
        suffix_sums = [sum(min_heap)]  # Sum of n smallest elements in last n positions

        for v in nums[2*n-1:n-1:-1]:
            current_sum = suffix_sums[-1]
            # If current element is larger than the smallest element in our heap
            if v > min_heap[0]:
                # Remove smallest element from sum
                current_sum -= heappop(min_heap)
                # Add current element to heap and sum
                heappush(min_heap, v)
                current_sum += v
            suffix_sums.append(current_sum)

        # Reverse suffix sums to match prefix sums order
        suffix_sums = suffix_sums[::-1]

        # Find minimum difference between prefix and suffix sums
        return min(p - s for p, s in zip(prefix_sums, suffix_sums))
