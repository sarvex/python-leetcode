class Solution:
    def maxNumberOfApples(self, weight: list[int]) -> int:
        """Maximum apples fitting in a basket with weight limit 5000.

        Intuition:
            Greedily pick the lightest apples first to maximize the count
            within the weight constraint.

        Approach:
            Sort weights in ascending order. Accumulate weights until the sum
            exceeds 5000, then return the count of apples added so far.

        Complexity:
            Time: O(n log n)
            Space: O(1)
        """
        weight.sort()
        total_weight = 0
        for i, apple_weight in enumerate(weight):
            total_weight += apple_weight
            if total_weight > 5000:
                return i
        return len(weight)
