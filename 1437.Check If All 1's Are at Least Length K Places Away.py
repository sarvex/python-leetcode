from math import inf


class Solution:
    def kLengthApart(self, nums: list[int], k: int) -> bool:
        """Check if all 1s are at least k places apart.

        Intuition:
            Track the index of the last seen 1 and verify each new 1 is at
            least k positions away.

        Approach:
            Iterate through the array, recording the last position of a 1.
            For each subsequent 1, check the gap is at least k. Initialize
            the last position to negative infinity to handle the first 1.

        Complexity:
            Time: O(n)
            Space: O(1)
        """
        last_one_index = -inf
        for index, value in enumerate(nums):
            if value:
                if index - last_one_index - 1 < k:
                    return False
                last_one_index = index
        return True
