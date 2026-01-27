from heapq import nlargest


class Solution:
    def dominantIndex(self, nums: list[int]) -> int:
        """Check if the largest element is at least twice the second largest.

        Intuition:
            Only the two largest values matter; extract them and compare.

        Approach:
            1. Find the two largest values using nlargest.
            2. If the largest is at least twice the second largest, return its index.

        Complexity:
            Time: O(N)
            Space: O(1)
        """
        largest, second_largest = nlargest(2, nums)
        return nums.index(largest) if largest >= 2 * second_largest else -1
