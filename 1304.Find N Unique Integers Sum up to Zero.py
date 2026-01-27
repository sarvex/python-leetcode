class Solution:
    def sumZero(self, n: int) -> list[int]:
        """Find n unique integers that sum to zero.

        Intuition:
            Pair positive and negative integers to cancel out, and add zero if n is odd.

        Approach:
            Generate pairs (i, -i) for i from 1 to n//2. If n is odd, include 0.

        Complexity:
            Time: O(n)
            Space: O(n)
        """
        result: list[int] = []
        for i in range(n >> 1):
            result.append(i + 1)
            result.append(-(i + 1))
        if n & 1:
            result.append(0)
        return result
