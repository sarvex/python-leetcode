class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        """Count integers in range whose popcount is prime.

        Intuition:
            Numbers up to 10^6 have at most 20 bits, so the set of possible
            prime popcounts is small and fixed.

        Approach:
            1. Precompute the set of primes up to 20.
            2. For each number in [left, right], check if its bit_count is in
               the prime set.

        Complexity:
            Time: O(R - L)
            Space: O(1)
        """
        prime_bits = {2, 3, 5, 7, 11, 13, 17, 19}
        return sum(i.bit_count() in prime_bits for i in range(left, right + 1))
