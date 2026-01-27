class Solution:
    def minKBitFlips(self, nums: list[int], k: int) -> int:
        """Find minimum k-bit flips to make all bits equal to 1.

        Intuition:
            Greedily flip starting at the leftmost 0. Use a difference array to
            track the cumulative number of flips affecting each position without
            re-scanning.

        Approach:
            Maintain a difference array and a running flip sum. At each index,
            if the effective value is 0, initiate a flip of length k. If a flip
            would exceed the array bounds, return -1.

        Complexity:
            Time: O(n) single pass through the array
            Space: O(n) for the difference array
        """
        length = len(nums)
        diff = [0] * (length + 1)
        flips = flip_sum = 0
        for i, value in enumerate(nums):
            flip_sum += diff[i]
            if flip_sum % 2 == value:
                if i + k > length:
                    return -1
                diff[i] += 1
                diff[i + k] -= 1
                flip_sum += 1
                flips += 1
        return flips
