class Solution:
    def numTeams(self, rating: list[int]) -> int:
        """Count teams of 3 soldiers with increasing or decreasing ratings.

        Intuition:
            For each middle element, count how many valid left and right
            elements can form increasing or decreasing triplets.

        Approach:
            For each element as the middle of the triplet, count elements
            smaller on the left and larger on the right (increasing), plus
            elements larger on the left and smaller on the right (decreasing).

        Complexity:
            Time: O(n^2) iterating pairs for each middle element
            Space: O(1) auxiliary space
        """
        result, length = 0, len(rating)
        for i, middle in enumerate(rating):
            left_smaller = sum(left < middle for left in rating[:i])
            right_larger = sum(right > middle for right in rating[i + 1 :])
            result += left_smaller * right_larger
            result += (i - left_smaller) * (length - i - 1 - right_larger)
        return result
