class Solution:
    def totalHammingDistance(self, nums: list[int]) -> int:
        """Bit-position counting for total pairwise Hamming distance.

        Intuition:
            For each bit position, count how many numbers have that bit set.
            The contribution to total Hamming distance is set_count *
            unset_count for that position.

        Approach:
            For each of 32 bit positions, count how many numbers have the
            bit set. Multiply by the count of numbers without that bit set
            and accumulate.

        Complexity:
            Time: O(32 * n) = O(n)
            Space: O(1)
        """
        total_distance, count = 0, len(nums)
        for bit in range(32):
            ones = sum(x >> bit & 1 for x in nums)
            zeros = count - ones
            total_distance += ones * zeros
        return total_distance
