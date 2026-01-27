class Solution:
    def sumSubarrayMins(self, arr: list[int]) -> int:
        """Monotonic stack to find contribution of each element as subarray minimum.

        Intuition:
            Each element contributes to multiple subarrays as the minimum.
            Using monotonic stacks, we can find the nearest smaller element
            on both sides to determine the range of subarrays where each
            element is the minimum.

        Approach:
            1. Use a monotonic increasing stack to find the previous less
               element index (left boundary) for each element.
            2. Use another pass to find the next less-or-equal element index
               (right boundary) for each element.
            3. Each element's contribution is value * left_count * right_count.
            4. Sum all contributions modulo 10^9 + 7.

        Complexity:
            Time: O(n)
            Space: O(n)
        """
        length = len(arr)
        prev_smaller = [-1] * length
        next_smaller = [length] * length
        stack: list[int] = []
        for idx, value in enumerate(arr):
            while stack and arr[stack[-1]] >= value:
                stack.pop()
            if stack:
                prev_smaller[idx] = stack[-1]
            stack.append(idx)

        stack = []
        for idx in range(length - 1, -1, -1):
            while stack and arr[stack[-1]] > arr[idx]:
                stack.pop()
            if stack:
                next_smaller[idx] = stack[-1]
            stack.append(idx)

        modulo = 10**9 + 7
        return (
            sum(
                (idx - prev_smaller[idx]) * (next_smaller[idx] - idx) * value
                for idx, value in enumerate(arr)
            )
            % modulo
        )
