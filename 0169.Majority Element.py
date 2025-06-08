from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """Boyer-Moore Voting Algorithm to find the majority element.

        Intuition:
        The majority element appears more than n/2 times, so its occurrences
        will exceed the combined occurrences of all other elements.

        Approach:
        Use the Boyer-Moore voting algorithm which maintains a candidate and a counter.
        When we encounter the candidate, we increment the counter; otherwise, we decrement it.
        If the counter reaches zero, we choose a new candidate.
        Since the majority element appears more than n/2 times, it will always be the final candidate.

        Complexity:
        Time: O(n) where n is the length of the input array
        Space: O(1) as we only use two variables regardless of input size
        """
        candidate = count = 0

        for num in nums:
            if count == 0:
                candidate = num
                count = 1
            else:
                count += 1 if candidate == num else -1

        return candidate
