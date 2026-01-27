from collections import defaultdict
from math import inf


class Solution:
    def minTransfers(self, transactions: list[list[int]]) -> int:
        """Bitmask DP on net balances for minimum transactions.

        Intuition:
            Compute net balances for each person. The problem reduces to
            partitioning non-zero balances into groups that sum to zero,
            minimizing total transactions (group_size - 1 per group).

        Approach:
            Calculate net balances and filter out zeros. Use bitmask DP
            where dp[mask] is the minimum transactions to settle the subset.
            For each mask with zero sum, initialize to popcount - 1, then
            try splitting into sub-masks for a better result.

        Complexity:
            Time: O(3^m) where m is the number of non-zero balances
            Space: O(2^m)
        """
        balances = defaultdict(int)
        for sender, receiver, amount in transactions:
            balances[sender] -= amount
            balances[receiver] += amount
        debts = [amount for amount in balances.values() if amount]
        num_debts = len(debts)
        dp = [inf] * (1 << num_debts)
        dp[0] = 0
        for mask in range(1, 1 << num_debts):
            subset_sum = 0
            for j, amount in enumerate(debts):
                if mask >> j & 1:
                    subset_sum += amount
            if subset_sum == 0:
                dp[mask] = mask.bit_count() - 1
                submask = (mask - 1) & mask
                while submask > 0:
                    dp[mask] = min(dp[mask], dp[submask] + dp[mask ^ submask])
                    submask = (submask - 1) & mask
        return dp[-1]
