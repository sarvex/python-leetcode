class Solution:
    def wiggleSort(self, nums: list[int]) -> None:
        """Single-pass greedy swap to achieve wiggle order.

        Intuition:
            At each position, we only need to compare adjacent elements and
            swap if they violate the wiggle property: nums[0] <= nums[1] >=
            nums[2] <= nums[3] ...

        Approach:
            1. Iterate through the array starting at index 1.
            2. At odd indices, the element should be >= its predecessor; swap if not.
            3. At even indices, the element should be <= its predecessor; swap if not.

        Complexity:
            Time: O(n)
            Space: O(1)
        """
        for i in range(1, len(nums)):
            if (i % 2 == 1 and nums[i] < nums[i - 1]) or (
                i % 2 == 0 and nums[i] > nums[i - 1]
            ):
                nums[i], nums[i - 1] = nums[i - 1], nums[i]
