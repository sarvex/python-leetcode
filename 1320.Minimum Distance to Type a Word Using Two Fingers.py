from math import inf


class Solution:
    def minimumDistance(self, word: str) -> int:
        """Find minimum distance to type a word using two fingers on a 6-column keyboard.

        Intuition:
            Track positions of both fingers using DP. State is (letter index,
            finger1 position, finger2 position).

        Approach:
            3D DP where dp[i][f1][f2] is the minimum cost to type the first i
            characters with finger 1 at position f1 and finger 2 at f2.
            Transition: move either finger to type the next character.

        Complexity:
            Time: O(n * 26^2)
            Space: O(n * 26^2)
        """

        def distance(a: int, b: int) -> int:
            r1, c1 = divmod(a, 6)
            r2, c2 = divmod(b, 6)
            return abs(r1 - r2) + abs(c1 - c2)

        length = len(word)
        dp = [[[inf] * 26 for _ in range(26)] for _ in range(length)]
        first_key = ord(word[0]) - ord("A")
        for j in range(26):
            dp[0][first_key][j] = 0
            dp[0][j][first_key] = 0
        for i in range(1, length):
            prev_key = ord(word[i - 1]) - ord("A")
            curr_key = ord(word[i]) - ord("A")
            move_cost = distance(prev_key, curr_key)
            for j in range(26):
                dp[i][curr_key][j] = min(
                    dp[i][curr_key][j], dp[i - 1][prev_key][j] + move_cost
                )
                dp[i][j][curr_key] = min(
                    dp[i][j][curr_key], dp[i - 1][j][prev_key] + move_cost
                )
                if j == prev_key:
                    for k in range(26):
                        alt_cost = distance(k, curr_key)
                        dp[i][curr_key][j] = min(
                            dp[i][curr_key][j], dp[i - 1][k][prev_key] + alt_cost
                        )
                        dp[i][j][curr_key] = min(
                            dp[i][j][curr_key], dp[i - 1][prev_key][k] + alt_cost
                        )
        last_key = ord(word[-1]) - ord("A")
        best_a = min(dp[length - 1][last_key])
        best_b = min(dp[length - 1][j][last_key] for j in range(26))
        return int(min(best_a, best_b))
