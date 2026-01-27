class Solution:
    def bestRotation(self, nums: list[int]) -> int:
        """Difference array to find rotation maximizing score.

        Intuition:
            Each element contributes a score of 1 when its value is <= its index
            after rotation. We can compute the range of rotations that make each
            element score using a difference array.

        Approach:
            1. For each element, compute the range of rotations [left, right]
               where it scores a point.
            2. Mark +1 at left and -1 at right in a difference array.
            3. Compute prefix sums and find the rotation with maximum score.

        Complexity:
            Time: O(n)
            Space: O(n)
        """
        length = len(nums)
        max_score, best_rotation = -1, length
        diff = [0] * length
        for i, value in enumerate(nums):
            left = (i + 1) % length
            right = (length + i + 1 - value) % length
            diff[left] += 1
            diff[right] -= 1
        running_sum = 0
        for rotation, delta in enumerate(diff):
            running_sum += delta
            if running_sum > max_score:
                max_score = running_sum
                best_rotation = rotation
        return best_rotation
