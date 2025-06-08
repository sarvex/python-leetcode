from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """Three-step array reversal technique for in-place rotation.

        Intuition:
            When rotating an array by k positions, the last k elements move to the front,
            and the first n-k elements move to the end. Instead of moving elements one by one,
            we can use array reversal to achieve this efficiently.

        Approach:
            1. Normalize k to handle cases where k > length of array
            2. Reverse the entire array
            3. Reverse the first k elements
            4. Reverse the remaining n-k elements

            Example with [1,2,3,4,5,6,7] and k=3:
            - After full reversal: [7,6,5,4,3,2,1]
            - After reversing first k: [5,6,7,4,3,2,1]
            - After reversing remaining: [5,6,7,1,2,3,4]

        Complexity:
            Time: O(n) where n is the length of the array
            Space: O(1) as we perform the rotation in-place
        """
        def reverse(start: int, end: int) -> None:
            """Reverse elements in nums from index start to end (inclusive)."""
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start, end = start + 1, end - 1

        n = len(nums)
        # Early return for edge cases
        if not nums or n <= 1 or k % n == 0:
            return

        k %= n  # Normalize k for cases where k > n
        reverse(0, n - 1)  # Reverse entire array
        reverse(0, k - 1)  # Reverse first k elements
        reverse(k, n - 1)  # Reverse remaining n-k elements
    def rotate_slice(self, nums: List[int], k: int) -> None:
        """Pythonic slice-based array rotation.

        Intuition:
            Python's slicing can be used to efficiently rotate an array by creating
            a new arrangement and assigning it back to the original array reference.

        Approach:
            1. Normalize k to handle cases where k > length of array
            2. Use slice operations to rearrange the array:
               - Take the last k elements (nums[-k:])
               - Concatenate with the first n-k elements (nums[:-k])
               - Assign back to nums[:] to modify in-place

        Complexity:
            Time: O(n) where n is the length of the array
            Space: O(n) as we create a new array before assignment
        """
        n = len(nums)
        if not nums or n <= 1:
            return
        k %= n  # Normalize k
        nums[:] = nums[-k:] + nums[:-k]
