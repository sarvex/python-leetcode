class Solution:
    def findLongestChain(self, pairs: list[list[int]]) -> int:
        """Dynamic programming to find longest chain of non-overlapping pairs.

        Intuition:
        Sort pairs and use DP where dp[i] is the longest chain ending at pair i.
        A pair can extend another if the previous pair's end is less than the current start.

        Approach:
        1. Sort pairs by their first element.
        2. Initialize dp array with all 1s (each pair is a chain of length 1).
        3. For each pair, check all previous pairs for valid extensions.
        4. Return the maximum value in dp.

        Complexity:
        Time: O(n^2)
        Space: O(n)
        """
        pairs.sort()
        dp = [1] * len(pairs)
        for i, (start, _) in enumerate(pairs):
            for j, (_, prev_end) in enumerate(pairs[:i]):
                if prev_end < start:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)
