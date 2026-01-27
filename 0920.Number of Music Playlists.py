class Solution:
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        """Dynamic programming counting valid playlists with repeat constraint.

        Intuition:
            We need to count playlists of length 'goal' using exactly 'n'
            different songs where a song can be replayed only after k other
            songs have been played. DP on (playlist_length, unique_songs_used).

        Approach:
            1. Define dp[i][j] = number of playlists of length i using j unique songs.
            2. Transition: add a new song (n-j+1 choices) or replay an old song
               (j-k choices, only if j > k).
            3. Return dp[goal][n].

        Complexity:
            Time: O(goal * n)
            Space: O(goal * n)
        """
        modulo = 10**9 + 7
        dp = [[0] * (n + 1) for _ in range(goal + 1)]
        dp[0][0] = 1
        for playlist_len in range(1, goal + 1):
            for unique_songs in range(1, n + 1):
                dp[playlist_len][unique_songs] = dp[playlist_len - 1][
                    unique_songs - 1
                ] * (n - unique_songs + 1)
                if unique_songs > k:
                    dp[playlist_len][unique_songs] += dp[playlist_len - 1][
                        unique_songs
                    ] * (unique_songs - k)
                dp[playlist_len][unique_songs] %= modulo
        return dp[goal][n]
