class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        """Linear scan tracking current and maximum consecutive ones.

        Intuition:
            Simply count consecutive 1s, resetting the counter on 0, and
            track the maximum seen.

        Approach:
            Iterate through the array. Increment the counter for each 1,
            update the maximum, and reset to 0 on encountering a 0.

        Complexity:
            Time: O(n)
            Space: O(1)
        """
        max_count = current_count = 0
        for value in nums:
            if value:
                current_count += 1
                max_count = max(max_count, current_count)
            else:
                current_count = 0
        return max_count
