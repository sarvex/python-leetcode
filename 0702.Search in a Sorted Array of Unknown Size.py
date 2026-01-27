class Solution:
    def search(self, reader: "ArrayReader", target: int) -> int:
        """Binary search with exponential bound discovery for unknown-size array.

        Intuition:
            Since the array size is unknown, first find an upper bound by
            doubling the index until the value exceeds the target. Then apply
            standard binary search within the discovered range.

        Approach:
            1. Start with right = 1, double it while reader.get(right) < target.
            2. Set left = right // 2 as the lower bound.
            3. Binary search between left and right for the target.
            4. Return the index if found, otherwise -1.

        Complexity:
            Time: O(log n) for both bound discovery and binary search
            Space: O(1) constant extra space
        """
        right = 1
        while reader.get(right) < target:
            right <<= 1
        left = right >> 1
        while left < right:
            mid = (left + right) >> 1
            if reader.get(mid) >= target:
                right = mid
            else:
                left = mid + 1
        return left if reader.get(left) == target else -1
