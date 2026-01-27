class Solution:
    def divisorGame(self, n: int) -> bool:
        """Divisor Game with mathematical observation.

        Intuition:
            The player with an even number always wins. If n is even, pick 1
            to give the opponent an odd number, and vice versa.

        Approach:
            Return True if n is even, since the first player can always force
            the opponent into an odd position, eventually leading to n=1 loss.

        Complexity:
            Time: O(1)
            Space: O(1)
        """
        return n % 2 == 0
