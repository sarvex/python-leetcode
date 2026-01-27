class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """Dutch National Flag Algorithm

        Intuition:
            Partition the array into three sections (0s, 1s, 2s) using
            three pointers in a single pass.

        Approach:
            Maintain a red pointer for the next 0 position, a blue pointer
            for the next 2 position, and a current pointer scanning left to
            right. Swap 0s to the front and 2s to the back. When a 2 is
            swapped in, re-examine the current position without advancing.

        Complexity:
            Time: O(n)
            Space: O(1)
        """
        red, blue, current = -1, len(nums), 0
        while current < blue:
            if nums[current] == 0:
                red += 1
                nums[red], nums[current] = nums[current], nums[red]
                current += 1
            elif nums[current] == 2:
                blue -= 1
                nums[blue], nums[current] = nums[current], nums[blue]
            else:
                current += 1
