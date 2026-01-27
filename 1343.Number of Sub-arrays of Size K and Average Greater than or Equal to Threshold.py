class Solution:
    def numOfSubarrays(self, arr: list[int], k: int, threshold: int) -> int:
        """Count subarrays of size k with average >= threshold.

        Intuition:
            Use a sliding window to maintain the running sum and compare
            against the threshold multiplied by k to avoid division.

        Approach:
            Compute the initial window sum, then slide by adding the new
            element and removing the old one. Count windows meeting the target.

        Complexity:
            Time: O(n)
            Space: O(1)
        """
        target = threshold * k
        window_sum = sum(arr[:k])
        count = int(window_sum >= target)
        for i in range(k, len(arr)):
            window_sum += arr[i] - arr[i - k]
            count += int(window_sum >= target)
        return count
