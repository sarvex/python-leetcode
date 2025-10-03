from typing import List
import heapq


class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        """
        Optimized heap-based approach for finding the largest perimeter triangle.

        Intuition:
        We need to find three numbers that can form a triangle with the largest possible perimeter.
        Using a heap allows us to efficiently examine the largest numbers first.

        Approach:
        Convert the array to a max-heap by negating all values (since heapq is a min-heap).
        Repeatedly check the three largest numbers to see if they satisfy the triangle inequality.
        If they do, return their sum. If not, remove the largest and try again.

        Complexity:
        Time: O(n log n) for heapify + O(n log n) for heap operations in worst case
        Space: O(n) for the heap
        """
        nums = [-num for num in nums]
        heapq.heapify(nums)

        while len(nums) >= 3:
            a = -heapq.heappop(nums)
            b = -heapq.heappop(nums)
            c = -nums[0]

            if b + c > a:
                return a + b + c

            heapq.heappush(nums, -b)

        return 0
