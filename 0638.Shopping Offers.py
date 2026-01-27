from functools import cache


class Solution:
    def shoppingOffers(
        self, price: list[int], special: list[list[int]], needs: list[int]
    ) -> int:
        """DFS with memoization using bitmask encoding of remaining needs.

        Intuition:
        Encode the needs vector as a bitmask (4 bits per item) and use memoized DFS
        to try all valid special offers, comparing against buying items individually.

        Approach:
        1. Encode needs into a single integer using 4-bit segments per item.
        2. For each state, compute the cost of buying items individually.
        3. Try each special offer if applicable and recurse on the reduced state.
        4. Return the minimum cost found.

        Complexity:
        Time: O(S * 2^(4*n)) where S is number of special offers, n is number of items
        Space: O(2^(4*n))
        """
        bits = 4

        @cache
        def dfs(current: int) -> int:
            individual_cost = sum(
                p * (current >> (i * bits) & 0xF) for i, p in enumerate(price)
            )
            for offer in special:
                next_state = current
                for j in range(len(needs)):
                    if (current >> (j * bits) & 0xF) < offer[j]:
                        break
                    next_state -= offer[j] << (j * bits)
                else:
                    individual_cost = min(individual_cost, offer[-1] + dfs(next_state))
            return individual_cost

        mask = 0
        for i, need in enumerate(needs):
            mask |= need << i * bits
        return dfs(mask)
