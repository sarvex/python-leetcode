class Solution:
    def numWays(self, n: int, k: int) -> int:
        """Dynamic programming tracking same-color and different-color paint choices.

        Intuition:
            At each fence post, we can either paint a different color from the
            previous post or the same color (only if the previous two are not
            the same). Track both states separately.

        Approach:
            1. Use two arrays: diff_color[i] for posts where post i differs from
               post i-1, and same_color[i] where they match.
            2. diff_color[i] = (diff_color[i-1] + same_color[i-1]) * (k - 1)
            3. same_color[i] = diff_color[i-1]
            4. Return the sum of both states for the last post.

        Complexity:
            Time: O(n)
            Space: O(n) for the DP arrays
        """
        diff_color = [0] * n
        same_color = [0] * n
        diff_color[0] = k
        for i in range(1, n):
            diff_color[i] = (diff_color[i - 1] + same_color[i - 1]) * (k - 1)
            same_color[i] = diff_color[i - 1]
        return diff_color[-1] + same_color[-1]
