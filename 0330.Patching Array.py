class Solution:
    def minPatches(self, nums: list[int], n: int) -> int:
        """Greedy patching to extend reachable range.

        Intuition:
            Track the smallest number we cannot yet form. If the next array
            element is within reach, extend the range; otherwise patch by
            doubling the reachable bound.

        Approach:
            1. Maintain `reachable` as the smallest unreachable sum (starts at 1).
            2. If nums[i] <= reachable, absorb it and extend the range.
            3. Otherwise, patch by adding `reachable` itself (doubling the range).
            4. Count the number of patches added.

        Complexity:
            Time: O(m + log n) where m is the length of nums
            Space: O(1)
        """
        reachable = 1
        patches = idx = 0
        while reachable <= n:
            if idx < len(nums) and nums[idx] <= reachable:
                reachable += nums[idx]
                idx += 1
            else:
                patches += 1
                reachable <<= 1
        return patches
