class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        """Hash map to track last seen index of each element.

        Intuition:
            Store the most recent index of each value. If a duplicate is found
            within distance k, return True.

        Approach:
            1. Iterate through the array, recording each value's index.
            2. If a value was seen before and the index difference <= k, return True.
            3. Update the stored index for the current value.

        Complexity:
            Time: O(n)
            Space: O(n)
        """
        last_seen: dict[int, int] = {}
        for idx, value in enumerate(nums):
            if value in last_seen and idx - last_seen[value] <= k:
                return True
            last_seen[value] = idx
        return False
