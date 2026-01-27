class Solution:
    def validMountainArray(self, arr: list[int]) -> bool:
        """Two-pointer climb from both ends to verify mountain shape.

        Intuition:
            A valid mountain has a strictly increasing left side and strictly
            decreasing right side. Walk inward from both ends and check they meet.

        Approach:
            1. Return False if array has fewer than 3 elements.
            2. Move left pointer up while values are strictly increasing.
            3. Move right pointer up while values are strictly decreasing.
            4. If both pointers meet at the same index (not at boundaries), it's valid.

        Complexity:
            Time: O(n) — single pass from both ends
            Space: O(1) — constant extra space
        """
        length = len(arr)
        if length < 3:
            return False
        left, right = 0, length - 1
        while left + 1 < length - 1 and arr[left] < arr[left + 1]:
            left += 1
        while right - 1 > 0 and arr[right - 1] > arr[right]:
            right -= 1
        return left == right
