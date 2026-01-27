class Solution:
    def isIdealPermutation(self, nums: list[int]) -> bool:
        """Check that every global inversion is also a local inversion.

        Intuition:
            A global inversion that is not local means some element at index i
            is greater than an element at index j where j >= i + 2. We track the
            prefix maximum up to index i-2 and check if it ever exceeds nums[i].

        Approach:
            1. Maintain the running maximum of nums[0..i-2]
            2. For each index i >= 2, check if prefix_max > nums[i]
            3. If so, a non-local global inversion exists — return False

        Complexity:
            Time: O(n)
            Space: O(1)
        """
        prefix_max = 0
        for i in range(2, len(nums)):
            if (prefix_max := max(prefix_max, nums[i - 2])) > nums[i]:
                return False
        return True
