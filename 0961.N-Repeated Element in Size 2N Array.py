class Solution:
    def repeatedNTimes(self, nums: list[int]) -> int:
        """Check nearby duplicates with gaps of 1, 2, and 3.

        Intuition:
            In an array of size 2n with n+1 unique elements where one repeats n times,
            there must be two occurrences within distance 3 of each other by pigeonhole.

        Approach:
            1. Check for duplicates at distance 1 (adjacent elements).
            2. Check for duplicates at distance 2.
            3. Check for duplicates at distance 3.
            4. Return the first duplicate found.

        Complexity:
            Time: O(n) — at most 3 passes through the array
            Space: O(1) — constant extra space
        """
        for gap in range(1, 4):
            for index in range(len(nums) - gap):
                if nums[index] == nums[index + gap]:
                    return nums[index]
        return -1
