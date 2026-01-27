from collections import Counter


class Solution:
    def isPossibleDivide(self, nums: list[int], k: int) -> bool:
        """Check if array can be divided into sets of k consecutive numbers.

        Intuition:
            Greedily form groups starting from the smallest available number.

        Approach:
            Count occurrences of each number. Iterate through sorted numbers and
            for each available number, try to form a consecutive group of size k
            by decrementing counts.

        Complexity:
            Time: O(n log n)
            Space: O(n)
        """
        frequency = Counter(nums)
        for value in sorted(nums):
            if frequency[value]:
                for consecutive in range(value, value + k):
                    if frequency[consecutive] == 0:
                        return False
                    frequency[consecutive] -= 1
                    if frequency[consecutive] == 0:
                        del frequency[consecutive]
        return True
