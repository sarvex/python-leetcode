from random import randint


class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        """Three-way quicksort with random pivot selection.

        Intuition:
            Quicksort with three-way partitioning handles duplicate elements
            efficiently. Random pivot selection avoids worst-case behavior
            on sorted or nearly sorted inputs.

        Approach:
            1. Choose a random pivot from the current range.
            2. Partition into three regions: less than, equal to, greater than.
            3. Recursively sort the less-than and greater-than regions.

        Complexity:
            Time: O(n log n) average
            Space: O(log n) for recursion stack
        """

        def quick_sort(low: int, high: int) -> None:
            if low >= high:
                return
            pivot = nums[randint(low, high)]
            less, greater, current = low - 1, high + 1, low
            while current < greater:
                if nums[current] < pivot:
                    nums[less + 1], nums[current] = nums[current], nums[less + 1]
                    less, current = less + 1, current + 1
                elif nums[current] > pivot:
                    greater -= 1
                    nums[greater], nums[current] = nums[current], nums[greater]
                else:
                    current = current + 1
            quick_sort(low, less)
            quick_sort(greater, high)

        quick_sort(0, len(nums) - 1)
        return nums
