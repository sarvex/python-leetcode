class Solution:
    def threeEqualParts(self, arr: list[int]) -> list[int]:
        """Find three equal binary parts by matching trailing bits.

        Intuition:
            If the array can be split into three parts with equal binary value,
            they must each contain the same number of 1-bits. We find the
            starting positions of each third of the 1-bits and verify equality.

        Approach:
            1. Count total ones; if not divisible by 3, return [-1, -1].
            2. If no ones, return [0, n-1].
            3. Find the start of each third (1st, cnt+1th, 2*cnt+1th one).
            4. Compare the three suffixes element by element.
            5. If they match until the end, return the split indices.

        Complexity:
            Time: O(n)
            Space: O(1)
        """

        def find_kth_one(target: int) -> int:
            ones_seen = 0
            for idx, value in enumerate(arr):
                ones_seen += value
                if ones_seen == target:
                    return idx
            return -1

        length = len(arr)
        total_ones, remainder = divmod(sum(arr), 3)
        if remainder:
            return [-1, -1]
        if total_ones == 0:
            return [0, length - 1]

        first_start = find_kth_one(1)
        second_start = find_kth_one(total_ones + 1)
        third_start = find_kth_one(total_ones * 2 + 1)
        while (
            third_start < length
            and arr[first_start] == arr[second_start] == arr[third_start]
        ):
            first_start, second_start, third_start = (
                first_start + 1,
                second_start + 1,
                third_start + 1,
            )
        return [first_start - 1, second_start] if third_start == length else [-1, -1]
