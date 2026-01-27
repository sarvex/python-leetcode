class Solution:
    def findContestMatch(self, n: int) -> str:
        """Simulate tournament bracket pairing from strongest to weakest.

        Intuition:
            In each round, pair the strongest remaining with the weakest.
            Repeat until one match remains.

        Approach:
            Start with team labels 1..n. Each round, pair team[i] with
            team[n-1-i] using parenthesized notation. Halve the count
            each round.

        Complexity:
            Time: O(n log n)
            Space: O(n)
        """
        teams = [str(i + 1) for i in range(n)]
        while n > 1:
            for i in range(n >> 1):
                teams[i] = f"({teams[i]},{teams[n - i - 1]})"
            n >>= 1
        return teams[0]
