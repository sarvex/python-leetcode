class Solution:
    def heightChecker(self, heights: list[int]) -> int:
        """Count positions where heights differ from sorted order.

        Intuition:
            Compare each student's height with the expected sorted position.

        Approach:
            Sort the heights array and count mismatches with the original.

        Complexity:
            Time: O(n log n) for sorting
            Space: O(n) for the sorted copy
        """
        expected = sorted(heights)
        return sum(a != b for a, b in zip(heights, expected))
