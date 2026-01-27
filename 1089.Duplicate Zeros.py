class Solution:
    def duplicateZeros(self, arr: list[int]) -> None:
        """Duplicate each zero in-place, shifting elements to the right.

        Intuition:
            Two-pass approach: first count how many elements fit after duplication,
            then fill from back to front.

        Approach:
            Pass 1: find the last element that fits in the array after zero
            duplication. Pass 2: copy elements from that position backward,
            duplicating zeros as encountered.

        Complexity:
            Time: O(n)
            Space: O(1)
        """
        n = len(arr)
        source, write_count = -1, 0
        while write_count < n:
            source += 1
            write_count += 1 if arr[source] else 2
        dest = n - 1
        if write_count == n + 1:
            arr[dest] = 0
            source, dest = source - 1, dest - 1
        while dest >= 0:
            if arr[source] == 0:
                arr[dest] = arr[dest - 1] = arr[source]
                dest -= 1
            else:
                arr[dest] = arr[source]
            source, dest = source - 1, dest - 1
