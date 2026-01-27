class Solution:
    def maxScore(self, cardPoints: list[int], k: int) -> int:
        """Maximize points by picking k cards from either end.

        Intuition:
            Taking k cards from the ends is equivalent to leaving a contiguous
            window of n-k cards. Use a sliding window approach.

        Approach:
            Start with the sum of the last k cards. Slide the window by
            adding one card from the left and removing one from the right,
            tracking the maximum sum.

        Complexity:
            Time: O(k) for the sliding window
            Space: O(1) auxiliary space
        """
        result = window_sum = sum(cardPoints[-k:])
        for i, value in enumerate(cardPoints[:k]):
            window_sum += value - cardPoints[-k + i]
            result = max(result, window_sum)
        return result
