class Solution:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:
        """Two-pointer partition for even and odd elements.

        Intuition:
            Use two pointers from both ends to swap odd elements at the left
            with even elements at the right, partitioning in-place.

        Approach:
            1. Initialize left pointer at start and right pointer at end.
            2. Move left forward while it points to even numbers.
            3. Move right backward while it points to odd numbers.
            4. Swap when left is odd and right is even, then advance both.

        Complexity:
            Time: O(n)
            Space: O(1)
        """
        left, right = 0, len(nums) - 1
        while left < right:
            if nums[left] % 2 == 0:
                left += 1
            elif nums[right] % 2 == 1:
                right -= 1
            else:
                nums[left], nums[right] = nums[right], nums[left]
                left, right = left + 1, right - 1
        return nums
