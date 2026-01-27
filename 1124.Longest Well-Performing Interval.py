class Solution:
    def longestWPI(self, hours: list[int]) -> int:
        """Find the longest well-performing interval in the work hours list.

        Intuition:
            Transform hours into +1/-1 based on the 8-hour threshold, then
            find the longest subarray with a positive prefix sum.

        Approach:
            Maintain a running prefix sum. If the sum is positive, the entire
            prefix is well-performing. Otherwise, look up the earliest index
            where the prefix sum was (current_sum - 1) using a hash map.

        Complexity:
            Time: O(n) where n is the length of hours
            Space: O(n) for the hash map of first occurrences
        """
        result = 0
        prefix_sum = 0
        first_occurrence: dict[int, int] = {}
        for i, hour in enumerate(hours):
            prefix_sum += 1 if hour > 8 else -1
            if prefix_sum > 0:
                result = i + 1
            elif prefix_sum - 1 in first_occurrence:
                result = max(result, i - first_occurrence[prefix_sum - 1])
            if prefix_sum not in first_occurrence:
                first_occurrence[prefix_sum] = i
        return result
