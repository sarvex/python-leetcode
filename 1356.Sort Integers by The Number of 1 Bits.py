class Solution:
    def sortByBits(self, arr: list[int]) -> list[int]:
        """Sort integers by the number of 1-bits, then by value.

        Intuition:
            Python's built-in sort with a composite key handles the
            two-level ordering naturally.

        Approach:
            Sort the array using a key of (bit_count, value) to achieve
            ascending order by number of set bits with ties broken by value.

        Complexity:
            Time: O(n log n)
            Space: O(n)
        """
        return sorted(arr, key=lambda x: (x.bit_count(), x))
