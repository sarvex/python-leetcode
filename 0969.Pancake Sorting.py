class Solution:
    def pancakeSort(self, arr: list[int]) -> list[int]:
        """Repeatedly flip the largest unsorted element into its correct position.

        Intuition:
        Like selection sort but using prefix reversals. For each position from
        the end, find the target value, flip it to the front, then flip it to
        its correct position.

        Approach:
        1. For each position i from n-1 down to 1, find where value i+1 is
        2. If not already in place, flip to front (if needed), then flip to position i
        3. Record each flip operation

        Complexity:
        Time: O(n^2) for finding and flipping each element
        Space: O(n) for the result list
        """

        def reverse_prefix(end: int) -> None:
            start = 0
            while start < end:
                arr[start], arr[end] = arr[end], arr[start]
                start, end = start + 1, end - 1

        length = len(arr)
        flips: list[int] = []
        for position in range(length - 1, 0, -1):
            target_index = position
            while target_index > 0 and arr[target_index] != position + 1:
                target_index -= 1
            if target_index < position:
                if target_index > 0:
                    flips.append(target_index + 1)
                    reverse_prefix(target_index)
                flips.append(position + 1)
                reverse_prefix(position)
        return flips
