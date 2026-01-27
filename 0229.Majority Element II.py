class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        """Boyer-Moore voting algorithm extended for n/3 threshold.

        Intuition:
            There can be at most two elements appearing more than n/3 times.
            Use two candidate counters to find them, then verify.

        Approach:
            1. Maintain two candidates with their counts.
            2. For each number, increment matching candidate or decrement both
               if neither matches (when both have nonzero counts).
            3. Verify candidates by counting actual occurrences.

        Complexity:
            Time: O(n)
            Space: O(1)
        """
        count1 = count2 = 0
        candidate1, candidate2 = 0, 1
        for num in nums:
            if num == candidate1:
                count1 += 1
            elif num == candidate2:
                count2 += 1
            elif count1 == 0:
                candidate1, count1 = num, 1
            elif count2 == 0:
                candidate2, count2 = num, 1
            else:
                count1, count2 = count1 - 1, count2 - 1
        return [
            candidate
            for candidate in [candidate1, candidate2]
            if nums.count(candidate) > len(nums) // 3
        ]
