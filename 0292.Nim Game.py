class Solution:
    def canWinNim(self, n: int) -> bool:
        """Mathematical game theory observation for Nim.

        Intuition:
            If the number of stones is a multiple of 4, the first player always
            loses because whatever they take (1-3), the opponent can take the
            complement to 4, eventually leaving the first player with 0.

        Approach:
            Return True if n is not divisible by 4.

        Complexity:
            Time: O(1)
            Space: O(1)
        """
        return n % 4 != 0
