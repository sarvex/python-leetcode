class Solution:
    def binaryGap(self, n: int) -> int:
        """Bit iteration tracking last set bit position.

        Intuition:
            Iterate through each bit of n and track the position of the last
            set bit to compute distances between consecutive ones.

        Approach:
            1. Iterate through all 32 bits of the integer.
            2. When a set bit is found, compute the distance from the previous
               set bit and update the maximum gap.
            3. Track the position of the last set bit seen.

        Complexity:
            Time: O(log n) — at most 32 iterations for a 32-bit integer.
            Space: O(1)
        """
        max_gap = 0
        last_one_position = -1
        for bit_index in range(32):
            if n & 1:
                if last_one_position != -1:
                    max_gap = max(max_gap, bit_index - last_one_position)
                last_one_position = bit_index
            n >>= 1
        return max_gap
