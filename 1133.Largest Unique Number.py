from collections import Counter


class Solution:
    def largestUniqueNumber(self, nums: list[int]) -> int:
        """Return the largest number that appears exactly once.

        Intuition:
            Count occurrences and filter for unique elements, then find the max.

        Approach:
            Use a Counter to tally frequencies. Return the maximum among
            elements with count 1, or -1 if none exist.

        Complexity:
            Time: O(n) where n is the length of nums
            Space: O(n) for the counter
        """
        frequency = Counter(nums)
        return max((num for num, count in frequency.items() if count == 1), default=-1)
