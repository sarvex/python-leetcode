class Solution:
    def sortArrayByParityII(self, nums: list[int]) -> list[int]:
        """Two-pointer swap placing odds and evens at correct indices.

        Intuition:
            Scan even indices for misplaced odd numbers. When found, find the
            next misplaced even number at an odd index and swap them.

        Approach:
            1. Maintain an odd-index pointer starting at 1.
            2. For each even index, if the value is odd, advance the odd pointer
               until finding an even value, then swap.
            3. This ensures all even indices have even values and odd indices
               have odd values.

        Complexity:
            Time: O(n)
            Space: O(1)
        """
        length = len(nums)
        odd_ptr = 1
        for even_idx in range(0, length, 2):
            if nums[even_idx] % 2:
                while nums[odd_ptr] % 2:
                    odd_ptr += 2
                nums[even_idx], nums[odd_ptr] = nums[odd_ptr], nums[even_idx]
        return nums
