class Solution:
    def numTrees(self, n: int) -> int:
        """Dynamic Programming with Catalan Numbers

        Intuition:
            The number of unique BSTs for n nodes follows the Catalan number
            pattern. For each root value i, the left subtree has i-1 nodes and
            the right subtree has n-i nodes, giving a recursive structure.

        Approach:
            Build a DP table where dp[i] represents the number of unique BSTs
            with i nodes. For each count i, iterate over all possible left
            subtree sizes j and multiply dp[j] * dp[i-j-1] to account for
            all combinations of left and right subtrees.

        Complexity:
            Time: O(n^2)
            Space: O(n)
        """
        dp = [1] + [0] * n
        for i in range(n + 1):
            for j in range(i):
                dp[i] += dp[j] * dp[i - j - 1]
        return dp[n]
