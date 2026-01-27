class Solution:
    def maxSatisfaction(self, satisfaction: list[int]) -> int:
        """Maximize the like-time coefficient sum by selecting dishes.

        Intuition:
            Sort dishes in descending order and greedily add dishes as long
            as the running sum remains positive.

        Approach:
            Sort satisfaction in descending order. Accumulate a running sum
            of satisfaction values. For each dish, if adding it keeps the
            running sum positive, add the running sum to the answer.

        Complexity:
            Time: O(n log n) for sorting
            Space: O(1) auxiliary space (in-place sort)
        """
        satisfaction.sort(reverse=True)
        result = running_sum = 0
        for value in satisfaction:
            running_sum += value
            if running_sum <= 0:
                break
            result += running_sum
        return result
