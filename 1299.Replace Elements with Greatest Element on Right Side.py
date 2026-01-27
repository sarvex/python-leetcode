class Solution:
    def replaceElements(self, arr: list[int]) -> list[int]:
        """Replace each element with the greatest element on its right side.

        Intuition:
            Traverse from right to left, tracking the running maximum to replace
            each element in a single pass.

        Approach:
            Iterate backwards, maintaining the maximum seen so far. Replace each
            element with the current maximum, then update the maximum.

        Complexity:
            Time: O(n)
            Space: O(1)
        """
        right_max = -1
        for i in range(len(arr) - 1, -1, -1):
            current = arr[i]
            arr[i] = right_max
            right_max = max(right_max, current)
        return arr
