class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        """Bit manipulation approach to find minimum flips needed.

        Intuition:
        Since we need to make (a OR b) equal to c, we need to check each bit position
        and determine how many flips are needed at that position.

        Approach:
        1. Iterate through each bit position (0-31 for 32-bit integers)
        2. For each position, extract the corresponding bit from a, b, and c
        3. If c's bit is 0, both a and b's bits must be 0, so count flips needed
        4. If c's bit is 1, at least one of a or b's bits must be 1, so count if both are 0
        5. Sum up all required flips

        Complexity:
        Time: O(1) - We always iterate through 32 bits regardless of input size
        Space: O(1) - We use constant extra space
        """
        flips = 0
        for i in range(32):
            x, y, z = a >> i & 1, b >> i & 1, c >> i & 1
            flips += x + y if z == 0 else int(x == 0 and y == 0)
        return flips
