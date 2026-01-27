class Solution:
    def maxScoreSightseeingPair(self, values: list[int]) -> int:
        """Find the maximum score of a sightseeing pair values[i]+values[j]+i-j.

        Intuition:
            Decompose the score as (values[i]+i) + (values[j]-j). Track the
            best (values[i]+i) seen so far while iterating j.

        Approach:
            Maintain the maximum of values[i]+i for all previous indices. For
            each j, compute the candidate score and update the running maximum.

        Complexity:
            Time: O(n) single pass
            Space: O(1)
        """
        best_score = 0
        max_left = values[0]
        for j in range(1, len(values)):
            best_score = max(best_score, values[j] - j + max_left)
            max_left = max(max_left, values[j] + j)
        return best_score
