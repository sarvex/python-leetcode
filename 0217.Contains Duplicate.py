class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        """Set comparison to detect duplicate elements.

        Intuition:
            A set removes duplicates, so if its size differs from the list,
            duplicates exist.

        Approach:
            1. Convert the list to a set.
            2. Compare lengths of the set and original list.

        Complexity:
            Time: O(n)
            Space: O(n)
        """
        return len(set(nums)) != len(nums)
