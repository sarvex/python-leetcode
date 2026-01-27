class Solution:
    def numDecodings(self, s: str) -> int:
        """Space-optimized DP handling wildcard '*' in decode ways.

        Intuition:
        Extend the decode ways problem to handle '*' wildcards that can represent
        digits 1-9, tracking transitions for both single and two-digit decodings.

        Approach:
        1. Use three rolling variables for dp[i-2], dp[i-1], dp[i].
        2. For single digit: '*' contributes 9 ways, non-zero digit contributes 1.
        3. For two digits: enumerate valid combinations with '*' and digit pairs.
        4. Apply modular arithmetic throughout.

        Complexity:
        Time: O(n)
        Space: O(1)
        """
        mod = int(1e9 + 7)
        length = len(s)

        two_back, one_back, current = 0, 1, 0
        for i in range(1, length + 1):
            if s[i - 1] == "*":
                current = 9 * one_back % mod
            elif s[i - 1] != "0":
                current = one_back
            else:
                current = 0

            if i > 1:
                if s[i - 2] == "*" and s[i - 1] == "*":
                    current = (current + 15 * two_back) % mod
                elif s[i - 2] == "*":
                    if s[i - 1] > "6":
                        current = (current + two_back) % mod
                    else:
                        current = (current + 2 * two_back) % mod
                elif s[i - 1] == "*":
                    if s[i - 2] == "1":
                        current = (current + 9 * two_back) % mod
                    elif s[i - 2] == "2":
                        current = (current + 6 * two_back) % mod
                elif (
                    s[i - 2] != "0"
                    and (ord(s[i - 2]) - ord("0")) * 10 + ord(s[i - 1]) - ord("0") <= 26
                ):
                    current = (current + two_back) % mod

            two_back, one_back = one_back, current

        return current
