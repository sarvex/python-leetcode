class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        """Two-pointer merge from both ends to produce sorted squares.

        Intuition:
        In a sorted array, the largest squares are at the extremes (most
        negative or most positive). Using two pointers from both ends and
        building the result in reverse gives a sorted output.

        Approach:
        1. Place pointers at the start and end of the array
        2. Compare absolute values (via squares) at both pointers
        3. Append the larger square and move that pointer inward
        4. Reverse the result to get ascending order

        Complexity:
        Time: O(n) where n is the array length
        Space: O(n) for the result array
        """
        result: list[int] = []
        left, right = 0, len(nums) - 1
        while left <= right:
            left_square = nums[left] * nums[left]
            right_square = nums[right] * nums[right]
            if left_square > right_square:
                result.append(left_square)
                left += 1
            else:
                result.append(right_square)
                right -= 1
        return result[::-1]
