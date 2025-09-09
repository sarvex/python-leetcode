class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        dp = [0] * n
        dp[0] = 1
        s = 0
        mod = 10**9 + 7
        
        for i in range(delay, n):
            s = (s + dp[i - delay]) % mod
            if i - forget >= 0:
                s = (s - dp[i - forget] + mod) % mod
            dp[i] = s
        
        return sum(dp[-forget:]) % mod