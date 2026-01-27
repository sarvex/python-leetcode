class Solution:
    def racecar(self, target: int) -> int:
        """Bottom-up DP for minimum instructions to reach target position.

        Intuition:
            If target is exactly 2^k - 1, we need k 'A' instructions.
            Otherwise, we either overshoot and reverse, or undershoot with
            a reverse and then continue forward.

        Approach:
            1. For each position i from 1 to target, compute dp[i].
            2. If i == 2^k - 1, dp[i] = k (all accelerate).
            3. Otherwise, try overshooting: go 2^k - 1, reverse, solve remainder.
            4. Also try undershooting: go 2^(k-1) - 2^j, reverse, then continue.

        Complexity:
            Time: O(target * log(target))
            Space: O(target)
        """
        dp = [0] * (target + 1)
        for position in range(1, target + 1):
            num_bits = position.bit_length()
            if position == 2**num_bits - 1:
                dp[position] = num_bits
                continue
            dp[position] = dp[2**num_bits - 1 - position] + num_bits + 1
            for back_bits in range(num_bits - 1):
                overshoot_dist = position - (2 ** (num_bits - 1) - 2**back_bits)
                dp[position] = min(
                    dp[position], dp[overshoot_dist] + num_bits - 1 + back_bits + 2
                )
        return dp[target]
