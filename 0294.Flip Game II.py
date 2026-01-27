from functools import cache


class Solution:
    def canWin(self, currentState: str) -> bool:
        """Bitmask game theory with memoized DFS.

        Intuition:
            Represent the board as a bitmask where each bit indicates '+'.
            A player wins if there exists a move after which the opponent
            cannot win.

        Approach:
            1. Encode the initial state as a bitmask of '+' positions.
            2. Use memoized DFS on the bitmask.
            3. For each pair of adjacent set bits, flip them and check if the
               opponent loses from the resulting state.
            4. If any move leads to opponent losing, current player wins.

        Complexity:
            Time: O(2^n) with memoization where n is string length
            Space: O(2^n)
        """
        length = len(currentState)

        @cache
        def dfs(bitmask: int) -> bool:
            for i in range(length - 1):
                if (bitmask & (1 << i)) == 0 or (bitmask & (1 << (i + 1)) == 0):
                    continue
                if dfs(bitmask ^ (1 << i) ^ (1 << (i + 1))):
                    continue
                return True
            return False

        bitmask = 0
        for i, char in enumerate(currentState):
            if char == "+":
                bitmask |= 1 << i
        return dfs(bitmask)
