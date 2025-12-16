from typing import List
import math


class Solution:
    def maximumProfit(
        self,
        n: int,
        present: List[int],
        future: List[int],
        hierarchy: List[List[int]],
        budget: int,
    ) -> int:
        # Build adjacency list for the tree.
        # hierarchy contains [u, v] meaning u is boss of v.
        adj = [[] for _ in range(n + 1)]
        for u, v in hierarchy:
            adj[u].append(v)

        # Helper function to merge two DP arrays (Knapsack merge)
        # dp1, dp2: list where index is cost and value is max profit. -1 if unreachable.
        def merge(dp1, dp2):
            new_dp = [-1] * (budget + 1)
            # Collect reachable states to optimize inner loops
            # This reduces complexity from O(Budget^2) to O(Size(dp1)*Size(dp2))
            states1 = [(c, p) for c, p in enumerate(dp1) if p != -1]
            states2 = [(c, p) for c, p in enumerate(dp2) if p != -1]

            for c1, p1 in states1:
                for c2, p2 in states2:
                    if c1 + c2 <= budget:
                        if p1 + p2 > new_dp[c1 + c2]:
                            new_dp[c1 + c2] = p1 + p2
            return new_dp

        # DFS function
        # Returns a tuple of two DP lists:
        # 1. dp_if_parent_did_not_buy: Max profit from subtree u given parent(u) did NOT buy.
        # 2. dp_if_parent_did_buy: Max profit from subtree u given parent(u) DID buy.
        def dfs(u):
            # Base DP for accumulating children results.
            # Initial state: 0 cost, 0 profit.

            # combined_children_buy: aggregated results from children assuming u BOUGHT
            combined_children_buy = [-1] * (budget + 1)
            combined_children_buy[0] = 0

            # combined_children_no_buy: aggregated results from children assuming u DID NOT BUY
            combined_children_no_buy = [-1] * (budget + 1)
            combined_children_no_buy[0] = 0

            # Process all children first (Post-order)
            for v in adj[u]:
                child_res_no_buy, child_res_buy = dfs(v)

                # If u buys, v sees its parent (u) bought -> use child_res_buy
                combined_children_buy = merge(combined_children_buy, child_res_buy)

                # If u doesn't buy, v sees its parent (u) didn't buy -> use child_res_no_buy
                combined_children_no_buy = merge(
                    combined_children_no_buy, child_res_no_buy
                )

            # Calculate costs and profits for u
            # Note: present/future are 0-indexed, u is 1-indexed
            idx = u - 1
            cost_full = present[idx]
            profit_full = future[idx] - present[idx]

            # Floor division for discount
            cost_discount = present[idx] // 2
            profit_discount = future[idx] - cost_discount

            # Construct result DPs for u

            # Case 1: Parent(u) did NOT buy
            # Option A: u doesn't buy. u contributes 0 cost 0 profit. Children see u didn't buy.
            #          -> Use combined_children_no_buy
            dp_parent_not = list(combined_children_no_buy)

            # Option B: u buys (Full Price). Children see u bought.
            #          -> Use combined_children_buy, shifted by cost_full, add profit_full
            if cost_full <= budget:
                for c, p in enumerate(combined_children_buy):
                    if p != -1:
                        if c + cost_full <= budget:
                            dp_parent_not[c + cost_full] = max(
                                dp_parent_not[c + cost_full], p + profit_full
                            )

            # Case 2: Parent(u) DID buy
            # Option A: u doesn't buy. (Same as Case 1 Option A)
            dp_parent_did = list(combined_children_no_buy)

            # Option B: u buys (Discounted). Children see u bought.
            #          -> Use combined_children_buy, shifted by cost_discount, add profit_discount
            if cost_discount <= budget:
                for c, p in enumerate(combined_children_buy):
                    if p != -1:
                        if c + cost_discount <= budget:
                            dp_parent_did[c + cost_discount] = max(
                                dp_parent_did[c + cost_discount], p + profit_discount
                            )

            return dp_parent_not, dp_parent_did

        # Start DFS from root (employee 1)
        # Root has no parent, so use the "parent not bought" result (idx 0 of return)
        final_dp, _ = dfs(1)

        return max(final_dp)
