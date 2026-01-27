class Solution:
    def canBeEqual(self, target: list[int], arr: list[int]) -> bool:
        """Check if arr can become target by reversing subarrays.

        Intuition:
            Any permutation is reachable through subarray reversals, so the
            arrays just need the same elements with the same frequencies.

        Approach:
            Sort both arrays and compare for equality.

        Complexity:
            Time: O(n log n) for sorting
            Space: O(n) for sorted copies
        """
        return sorted(target) == sorted(arr)
