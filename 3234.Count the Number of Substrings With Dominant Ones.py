from math import isqrt
from typing import List


class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        """Count substrings with dominant ones (ones >= zeros^2).

        Tagline: Split by zero-count threshold; combine combinatorics on ones-runs with sqrt decomposition.

        Intuition:
            Substrings are characterized by the number of zeros z and ones o. The condition o >= z^2 is strict for large z
            and lax for small z. Around zeros, ones appear in runs between zeros. For a fixed window of k zeros, the ones
            inside are fixed, while extra ones can be taken from the bordering runs. Counting valid border choices reduces
            to bounded integer pair sums.

        Approach:
            - Precompute positions of zeros and lengths of ones-runs between zeros (including ends), plus prefix sums and
              suffix maxima of runs.
            - Handle k = 0 (no zeros) by summing arithmetic series over ones-runs.
            - For small k in [1..B], where B = floor(sqrt(n)), slide a window across zeros. For each window:
                inner_ones = sum of runs strictly inside the window; left/right capacities are the adjacent runs.
                Count pairs (x, y) with x in [0..L], y in [0..R] such that x + y >= need, where need = max(0, k^2 - inner_ones).
                Use a closed-form for counting bounded pairs by sum.
            - For large k > B, iterate windows starting at each zero-index t and increasing k until no future window can
              be valid. Early-break using an upper bound with suffix max of right run.

        Complexity:
            Time: O(n * sqrt(n)) in worst case. Space: O(n) for runs and helpers.
        """

        n: int = len(s)
        if n == 0:
            return 0

        # Build zero positions with sentinels and ones-runs between zeros
        zeros: List[int] = [-1]
        for i, ch in enumerate(s):
            if ch == '0':
                zeros.append(i)
        zeros.append(n)

        z: int = len(zeros) - 2  # number of real zeros
        # runs[i] = number of ones between zeros[i] and zeros[i+1], for i in [0..z]
        runs: List[int] = []
        for i in range(len(zeros) - 1):
            runs.append(zeros[i + 1] - zeros[i] - 1)

        # Edge: no zeros -> all substrings are dominant
        if z == 0:
            L = runs[0]
            return L * (L + 1) // 2

        # Prefix sums of runs to get inner ones quickly
        pr: List[int] = [0] * (len(runs) + 1)
        for i, v in enumerate(runs):
            pr[i + 1] = pr[i] + v

        # Suffix max of runs for an optimistic bound on right capacity in future windows
        suf_max: List[int] = [0] * (len(runs) + 1)
        cur = 0
        for i in range(len(runs) - 1, -1, -1):
            if runs[i] > cur:
                cur = runs[i]
            suf_max[i] = cur

        def count_pairs_sum_leq(left_cap: int, right_cap: int, ssum: int) -> int:
            """Count pairs (x,y) with 0<=x<=L, 0<=y<=R, x+y <= ssum in O(1).

            Uses piecewise closed forms. Ensures L <= R by swapping.
            """

            if ssum < 0:
                return 0
            L, R = left_cap, right_cap
            if L > R:
                L, R = R, L
            # Case 1: entirely in rising triangle
            if ssum <= L:
                t = ssum + 1
                return t * (t + 1) // 2
            # Case 2: covers full small side, partial large side, no tail removal
            if ssum <= R:
                tri = (L + 1) * (L + 2) // 2
                extra = (ssum - L) * (L + 1)
                return tri + extra
            # Case 3: near full rectangle; subtract complementary small triangle
            total = (L + 1) * (R + 1)
            # complementary threshold
            comp = L + R - ssum - 1
            # comp is in [0..L-1]
            t = comp + 1
            subtract = t * (t + 1) // 2
            return total - subtract

        def count_pairs_sum_geq(left_cap: int, right_cap: int, need: int) -> int:
            """Count pairs (x,y) with 0<=x<=L, 0<=y<=R, x+y >= need in O(1)."""

            total = (left_cap + 1) * (right_cap + 1)
            return total - count_pairs_sum_leq(left_cap, right_cap, need - 1)

        ans: int = 0

        # k = 0 (pure ones substrings)
        for run_len in runs:
            ans += run_len * (run_len + 1) // 2

        # Small k via sqrt decomposition
        B: int = isqrt(n)
        if B > z:
            B = z

        for k in range(1, B + 1):
            # window covers zeros indices [t+1 .. t+k]
            for t in range(0, z - k + 1):
                left = runs[t]
                right = runs[t + k]
                inner = pr[t + k] - pr[t + 1]
                need = k * k - inner
                if need <= 0:
                    ans += (left + 1) * (right + 1)
                elif need <= left + right:
                    ans += count_pairs_sum_geq(left, right, need)
                # else: impossible

        # Large k with early break using suffix max
        for t in range(0, z - B + 1):
            left = runs[t]
            k = B + 1
            while t + k <= z:
                right = runs[t + k]
                inner = pr[t + k] - pr[t + 1]
                need = k * k - inner
                if need <= 0:
                    ans += (left + 1) * (right + 1)
                elif need <= left + right:
                    ans += count_pairs_sum_geq(left, right, need)
                # Early termination: even with best possible future right run, cannot meet need
                max_future_right = suf_max[t + k]
                if need > left + max_future_right:
                    break
                k += 1

        return ans

