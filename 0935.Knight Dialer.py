class Solution:
    def knightDialer(self, n: int) -> int:
        """Dynamic programming with state transition for knight moves on phone pad.

        Intuition:
            A knight on a phone dialpad can only move to certain positions from each
            digit. We can track how many numbers end at each digit after each hop.

        Approach:
            1. Initialize counts for all 10 digits as 1.
            2. For each step, compute new counts based on valid knight moves.
            3. Each digit maps to specific reachable digits (e.g., 0->4,6).
            4. Sum all counts after n-1 transitions modulo 10^9+7.

        Complexity:
            Time: O(n) — iterate n steps with constant work per step
            Space: O(1) — only two arrays of fixed size 10
        """
        if n == 1:
            return 10
        MOD = 10**9 + 7
        counts = [1] * 10
        for _ in range(n - 1):
            updated = [0] * 10
            updated[0] = counts[4] + counts[6]
            updated[1] = counts[6] + counts[8]
            updated[2] = counts[7] + counts[9]
            updated[3] = counts[4] + counts[8]
            updated[4] = counts[0] + counts[3] + counts[9]
            updated[6] = counts[0] + counts[1] + counts[7]
            updated[7] = counts[2] + counts[6]
            updated[8] = counts[1] + counts[3]
            updated[9] = counts[2] + counts[4]
            counts = updated
        return sum(updated) % MOD
