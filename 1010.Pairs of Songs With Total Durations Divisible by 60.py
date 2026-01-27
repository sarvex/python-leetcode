from collections import Counter


class Solution:
    def numPairsDivisibleBy60(self, time: list[int]) -> int:
        """Count pairs of songs whose total duration is divisible by 60.

        Intuition:
            Reduce each duration modulo 60. Pair (a, b) works when
            (a + b) % 60 == 0, so for remainder r we need remainder (60 - r) % 60.

        Approach:
            Build a frequency counter of remainders. For remainders 1..29, multiply
            with their complement. Handle the special cases of remainder 0 and 30
            using combinations C(n, 2).

        Complexity:
            Time: O(n) for building the counter plus O(1) for pairing
            Space: O(1) since the counter has at most 60 keys
        """
        remainder_count: Counter[int] = Counter(t % 60 for t in time)
        pairs = sum(remainder_count[r] * remainder_count[60 - r] for r in range(1, 30))
        pairs += remainder_count[0] * (remainder_count[0] - 1) // 2
        pairs += remainder_count[30] * (remainder_count[30] - 1) // 2
        return pairs
