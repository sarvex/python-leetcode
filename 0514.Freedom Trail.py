from collections import defaultdict
from math import inf


class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        """DP to find minimum steps to spell key by rotating ring.

        Intuition:
            At each step, we choose which occurrence of the required character
            on the ring to rotate to, minimizing total rotation distance.

        Approach:
            Precompute positions of each character. Use DP where dp[i][j] is
            the minimum cost to spell key[0..i] with the ring aligned at position j.
            Transition considers all positions of the previous character.

        Complexity:
            Time: O(m * n^2) where m = len(key), n = len(ring)
            Space: O(m * n)
        """
        key_len, ring_len = len(key), len(ring)
        char_positions: dict[str, list[int]] = defaultdict(list)
        for i, char in enumerate(ring):
            char_positions[char].append(i)
        dp = [[inf] * ring_len for _ in range(key_len)]
        for j in char_positions[key[0]]:
            dp[0][j] = min(j, ring_len - j) + 1
        for i in range(1, key_len):
            for j in char_positions[key[i]]:
                for k in char_positions[key[i - 1]]:
                    dp[i][j] = min(
                        dp[i][j],
                        dp[i - 1][k] + min(abs(j - k), ring_len - abs(j - k)) + 1,
                    )
        return min(dp[-1][j] for j in char_positions[key[-1]])
