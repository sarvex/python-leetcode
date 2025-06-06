from typing import List
import heapq
import random


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """Quick select approach for finding kth largest element

        Intuition:
        The kth largest element is equivalent to the (n-k)th smallest element.
        Quick select is based on the quicksort algorithm but only explores one partition.

        Approach:
        1. Use randomized quick select to find the kth largest element
        2. Partition the array around a pivot and recursively search in one partition
        3. Alternative implementations using heap and sorting are provided as well

        Complexity:
        Time: O(n) average case, O(n²) worst case
        Space: O(1) extra space (O(log n) for recursion stack)
        """
        return self._quick_select(nums, len(nums) - k)

    def _quick_select(self, nums: List[int], k: int) -> int:
        """Find the kth smallest element using quick select algorithm"""
        def partition(left: int, right: int) -> int:
            # Choose random pivot to avoid worst case
            pivot_idx = random.randint(left, right)
            pivot = nums[pivot_idx]
            # Move pivot to the end
            nums[pivot_idx], nums[right] = nums[right], nums[pivot_idx]

            # Partition array around pivot
            store_idx = left
            for i in range(left, right):
                if nums[i] <= pivot:
                    nums[store_idx], nums[i] = nums[i], nums[store_idx]
                    store_idx += 1

            # Move pivot to its final place
            nums[store_idx], nums[right] = nums[right], nums[store_idx]
            return store_idx

        def select(left: int, right: int) -> int:
            if left == right:
                return nums[left]

            # Get position of pivot after partition
            pivot_idx = partition(left, right)

            # If pivot is the target, return it
            if pivot_idx == k:
                return nums[pivot_idx]
            # If pivot is greater than target, search left side
            elif pivot_idx > k:
                return select(left, pivot_idx - 1)
            # If pivot is less than target, search right side
            else:
                return select(pivot_idx + 1, right)

        return select(0, len(nums) - 1)

    def findKthLargest_heap(self, nums: List[int], k: int) -> int:
        """Heap-based approach

        Complexity:
        Time: O(n + k log n)
        Space: O(n)
        """
        return heapq.nlargest(k, nums)[-1]

    def findKthLargest_sort(self, nums: List[int], k: int) -> int:
        """Sorting-based approach

        Complexity:
        Time: O(n log n)
        Space: O(1) or O(n) depending on sort implementation
        """
        return sorted(nums, reverse=True)[k-1]
