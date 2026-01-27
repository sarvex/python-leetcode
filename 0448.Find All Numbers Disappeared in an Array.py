class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        """Set-based lookup to find missing numbers from 1 to n.

        Intuition:
            Convert the array to a set for O(1) lookups, then check which
            numbers in [1, n] are absent.

        Approach:
            1. Create a set from nums for fast membership testing.
            2. Iterate from 1 to n and collect numbers not in the set.

        Complexity:
            Time: O(n) for set construction and iteration.
            Space: O(n) for the set.
        """
        present = set(nums)
        return [x for x in range(1, len(nums) + 1) if x not in present]
