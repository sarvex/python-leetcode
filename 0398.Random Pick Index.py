import random


class Solution:
    """Reservoir sampling for random index selection with equal probability."""

    def __init__(self, nums: list[int]) -> None:
        """Initialize with the given array."""
        self.nums = nums

    def pick(self, target: int) -> int:
        """Pick a random index of the target value using reservoir sampling.

        Intuition:
            Reservoir sampling allows picking uniformly at random from
            an unknown number of candidates in a single pass.

        Approach:
            1. Scan through the array, tracking how many times target appears.
            2. For the k-th occurrence, replace the answer with probability 1/k.
            3. This guarantees each valid index is chosen with equal probability.

        Complexity:
            Time: O(n)
            Space: O(1)
        """
        count = result = 0
        for i, value in enumerate(self.nums):
            if value == target:
                count += 1
                if random.randint(1, count) == count:
                    result = i
        return result
