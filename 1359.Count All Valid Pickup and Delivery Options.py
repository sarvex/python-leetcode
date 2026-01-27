class Solution:
    def countOrders(self, n: int) -> int:
        """Count all valid pickup and delivery orderings for n orders.

        Intuition:
            Each new order i has its pickup placed among existing items, and
            its delivery must come after its pickup. The i-th order can be
            interleaved in i * (2i - 1) ways.

        Approach:
            Iteratively multiply the result by i * (2i - 1) for i from 2 to n,
            taking modulo at each step to prevent overflow.

        Complexity:
            Time: O(n)
            Space: O(1)
        """
        MOD = 10**9 + 7
        result = 1
        for i in range(2, n + 1):
            result = (result * i * (2 * i - 1)) % MOD
        return result
