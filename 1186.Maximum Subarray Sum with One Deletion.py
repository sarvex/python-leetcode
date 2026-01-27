class Solution:
    def maximumSum(self, arr: list[int]) -> int:
        """Find maximum subarray sum allowing at most one element deletion.

        Intuition:
            For each index, consider deleting that element and combining the best
            subarray ending just before it with the best subarray starting just
            after it.

        Approach:
            Compute left[i] = max subarray sum ending at i (Kadane's forward) and
            right[i] = max subarray sum starting at i (Kadane's backward). The
            answer is the maximum of all left[i] values (no deletion) and
            left[i-1] + right[i+1] for each valid i (one deletion).

        Complexity:
            Time: O(n)
            Space: O(n)
        """
        n = len(arr)
        max_ending_here = [0] * n
        max_starting_here = [0] * n

        running_sum = 0
        for i, val in enumerate(arr):
            running_sum = max(running_sum, 0) + val
            max_ending_here[i] = running_sum

        running_sum = 0
        for i in range(n - 1, -1, -1):
            running_sum = max(running_sum, 0) + arr[i]
            max_starting_here[i] = running_sum

        result = max(max_ending_here)
        for i in range(1, n - 1):
            result = max(result, max_ending_here[i - 1] + max_starting_here[i + 1])
        return result
