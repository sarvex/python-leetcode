class Solution:
    def longestMountain(self, arr: list[int]) -> int:
        """Two-pass DP tracking increasing and decreasing run lengths.

        Intuition:
            Compute the length of increasing runs ending at each index and
            decreasing runs starting at each index. A mountain peak has both.

        Approach:
            1. Forward pass: compute increasing run length ending at each index.
            2. Backward pass: compute decreasing run length starting at each index.
            3. At each peak (both runs > 1), the mountain length is their sum - 1.

        Complexity:
            Time: O(n)
            Space: O(n)
        """
        length = len(arr)
        increasing = [1] * length
        decreasing = [1] * length
        for i in range(1, length):
            if arr[i] > arr[i - 1]:
                increasing[i] = increasing[i - 1] + 1
        result = 0
        for i in range(length - 2, -1, -1):
            if arr[i] > arr[i + 1]:
                decreasing[i] = decreasing[i + 1] + 1
                if increasing[i] > 1:
                    result = max(result, increasing[i] + decreasing[i] - 1)
        return result
