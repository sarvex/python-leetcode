class Solution:
    def sortTransformedArray(
        self, nums: list[int], a: int, b: int, c: int
    ) -> list[int]:
        """Sort quadratic transformation of sorted array using two pointers.

        Intuition:
            A quadratic function applied to a sorted array produces values that
            are either U-shaped (a > 0) or inverted-U-shaped (a < 0). The
            extremes are at the two ends of the array.

        Approach:
            Use two pointers at both ends of the array. If a >= 0, the largest
            values are at the ends, so fill the result from back to front.
            If a < 0, the smallest values are at the ends, so fill from front
            to back. Compare transformed values at both pointers each step.

        Complexity:
            Time: O(n)
            Space: O(n)
        """

        def transform(x: int) -> int:
            return a * x * x + b * x + c

        length = len(nums)
        left, right, pos = 0, length - 1, 0 if a < 0 else length - 1
        result = [0] * length
        while left <= right:
            val_left, val_right = transform(nums[left]), transform(nums[right])
            if a < 0:
                if val_left <= val_right:
                    result[pos] = val_left
                    left += 1
                else:
                    result[pos] = val_right
                    right -= 1
                pos += 1
            else:
                if val_left >= val_right:
                    result[pos] = val_left
                    left += 1
                else:
                    result[pos] = val_right
                    right -= 1
                pos -= 1
        return result
