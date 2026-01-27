from collections import defaultdict


class Solution:
    def numberWays(self, hats: list[list[int]]) -> int:
        """Count ways to assign distinct hats to people using bitmask DP.

        Intuition:
            Iterate over hats (up to 40) instead of people (up to 10) to keep
            the bitmask state small, representing which people have been assigned.

        Approach:
            Build a mapping from hat to list of people who like it. Use DP where
            dp[i][j] is the number of ways to assign hats 1..i such that the set
            of people with hats is represented by bitmask j. For each hat, either
            skip it or assign it to an eligible person.

        Complexity:
            Time: O(m * 2^n * n) where m is max hat number and n is number of people
            Space: O(m * 2^n)
        """
        hat_to_people: dict[int, list[int]] = defaultdict(list)
        for person_index, preferred_hats in enumerate(hats):
            for hat in preferred_hats:
                hat_to_people[hat].append(person_index)

        MOD = 10**9 + 7
        num_people = len(hats)
        max_hat = max(max(h) for h in hats)
        dp = [[0] * (1 << num_people) for _ in range(max_hat + 1)]
        dp[0][0] = 1

        for hat in range(1, max_hat + 1):
            for mask in range(1 << num_people):
                dp[hat][mask] = dp[hat - 1][mask]
                for person in hat_to_people[hat]:
                    if mask >> person & 1:
                        dp[hat][mask] = (
                            dp[hat][mask] + dp[hat - 1][mask ^ (1 << person)]
                        ) % MOD

        return dp[max_hat][-1]
