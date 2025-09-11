class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        """
        Tagline: Sliding-window DP on daily sharers using 1-based day indexing.
        
        Intuition:
            Track how many people learn the secret each day. On any day d, only
            those who learned in the window [d - forget + 1, d - delay] are able
            to share. We maintain a sliding count of such "current sharers".
        
        Approach:
            Let new[d] be the number of people who first learn the secret on day d.
            Initialize new[1] = 1. Maintain sharers = number of people eligible to
            share on day d. When advancing to day d:
              - Add new[d - delay] to sharers (they become eligible today).
              - Subtract new[d - forget] from sharers (they forget today).
            Then set new[d] = sharers. The final answer is the number of people who
            still remember the secret on day n, which equals the sum of new[d] for
            the last 'forget' days up to n.
        
        Complexity:
            Time: O(n)
            Space: O(n)
        """
        MOD = 1_000_000_007
        # 1-based indexing for clarity with problem statement days.
        new = [0] * (n + 1)
        new[1] = 1
        sharers = 0

        for day in range(2, n + 1):
            add_idx = day - delay
            rem_idx = day - forget
            if add_idx >= 1:
                sharers = (sharers + new[add_idx]) % MOD
            if rem_idx >= 1:
                sharers = (sharers - new[rem_idx]) % MOD
            new[day] = sharers

        start = max(1, n - forget + 1)
        return sum(new[start : n + 1]) % MOD