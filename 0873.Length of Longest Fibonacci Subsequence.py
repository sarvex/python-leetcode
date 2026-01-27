class Solution:
    def lenLongestFibSubseq(self, arr: list[int]) -> int:
        """Dynamic programming with value-to-index map for Fibonacci pairs.

        Intuition:
            For each pair (arr[j], arr[i]), check if arr[i] - arr[j] exists
            earlier in the array, extending a Fibonacci-like subsequence.

        Approach:
            1. Build a dictionary mapping each value to its index.
            2. Use a 2D DP table where dp[i][j] represents the length of
               the longest Fibonacci subsequence ending with arr[j] and arr[i].
            3. For each pair (i, j), compute the required predecessor and
               look it up in the dictionary to extend the chain.

        Complexity:
            Time: O(n^2)
            Space: O(n^2)
        """
        length = len(arr)
        dp = [[0] * length for _ in range(length)]
        value_to_index = {value: index for index, value in enumerate(arr)}
        for i in range(length):
            for j in range(i):
                dp[i][j] = 2
        longest = 0
        for i in range(2, length):
            for j in range(1, i):
                predecessor = arr[i] - arr[j]
                if (
                    predecessor in value_to_index
                    and (prev_index := value_to_index[predecessor]) < j
                ):
                    dp[i][j] = max(dp[i][j], dp[j][prev_index] + 1)
                    longest = max(longest, dp[i][j])
        return longest
