class Solution:
    def minMoves(self, nums: list[int]) -> int:
        """Incrementing n-1 elements is equivalent to decrementing one element.

        Intuition:
            Incrementing all but one element by 1 is the same as decrementing
            one element by 1. The total moves needed equals the sum of differences
            from the minimum value.

        Approach:
            1. Find the minimum value in the array.
            2. Return sum(nums) - min(nums) * len(nums), which is the total
               number of decrements needed to make all elements equal to min.

        Complexity:
            Time: O(n) for computing sum and min.
            Space: O(1) with no extra storage.
        """
        return sum(nums) - min(nums) * len(nums)
