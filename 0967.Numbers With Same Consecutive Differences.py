class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> list[int]:
        """DFS digit-by-digit construction ensuring consecutive digit difference equals k.

        Intuition:
        Build numbers digit by digit, ensuring each new digit differs from the
        previous by exactly k. DFS naturally explores all valid combinations.

        Approach:
        1. Start with digits 1-9 as the first digit (no leading zeros)
        2. For each position, try adding last_digit + k and last_digit - k
        3. Skip duplicate branches when k == 0
        4. Collect complete n-digit numbers

        Complexity:
        Time: O(2^n) in the worst case for branching at each digit
        Space: O(2^n) for the result list and recursion stack
        """
        result: list[int] = []

        def dfs(remaining: int, current: int) -> None:
            if remaining == 0:
                result.append(current)
                return
            last_digit = current % 10
            if last_digit + k <= 9:
                dfs(remaining - 1, current * 10 + last_digit + k)
            if last_digit - k >= 0 and k != 0:
                dfs(remaining - 1, current * 10 + last_digit - k)

        for digit in range(1, 10):
            dfs(n - 1, digit)
        return result
