from collections import Counter


class Solution:
    def rearrangeBarcodes(self, barcodes: list[int]) -> list[int]:
        """Rearrange barcodes so no two adjacent elements are equal.

        Intuition:
            Place most frequent elements first at even indices, then fill odd indices.

        Approach:
            Sort by frequency descending, then interleave by placing elements
            at even positions first, then odd positions.

        Complexity:
            Time: O(n log n) for sorting
            Space: O(n) for the result array
        """
        frequency = Counter(barcodes)
        barcodes.sort(key=lambda x: (-frequency[x], x))
        n = len(barcodes)
        result = [0] * n
        result[::2] = barcodes[: (n + 1) // 2]
        result[1::2] = barcodes[(n + 1) // 2 :]
        return result
