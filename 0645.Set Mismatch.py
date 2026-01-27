class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        """Math-based approach using sum differences to find duplicate and missing.

        Intuition:
        The duplicate causes the actual sum to exceed the set sum, and the missing
        number is the difference between the expected sum and the set sum.

        Approach:
        1. Compute expected sum s1 = n*(n+1)/2.
        2. Compute set sum s2 = sum of unique elements.
        3. Compute actual sum s = sum of all elements.
        4. Duplicate = s - s2, Missing = s1 - s2.

        Complexity:
        Time: O(n)
        Space: O(n)
        """
        length = len(nums)
        expected_sum = (1 + length) * length // 2
        unique_sum = sum(set(nums))
        actual_sum = sum(nums)
        return [actual_sum - unique_sum, expected_sum - unique_sum]
