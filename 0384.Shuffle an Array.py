import random


class Solution:
    """Shuffle an array using Fisher-Yates algorithm with reset capability."""

    def __init__(self, nums: list[int]) -> None:
        """Initialize with the original array."""
        self.nums = nums
        self.original = nums.copy()

    def reset(self) -> list[int]:
        """Reset the array to its original configuration.

        Intuition:
            Keep a copy of the original array to restore from.

        Approach:
            Copy the stored original back into the working array.

        Complexity:
            Time: O(n)
            Space: O(n)
        """
        self.nums = self.original.copy()
        return self.nums

    def shuffle(self) -> list[int]:
        """Return a random shuffling of the array.

        Intuition:
            Fisher-Yates shuffle guarantees uniform random permutation
            by swapping each element with a random subsequent element.

        Approach:
            For each index i, swap nums[i] with a randomly chosen element
            from index i to end.

        Complexity:
            Time: O(n)
            Space: O(1)
        """
        for i in range(len(self.nums)):
            swap_index = random.randrange(i, len(self.nums))
            self.nums[i], self.nums[swap_index] = self.nums[swap_index], self.nums[i]
        return self.nums
