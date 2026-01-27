from math import factorial


class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        """Count permutations where primes are at prime indices.

        Intuition:
            Primes must occupy prime-indexed positions and non-primes must occupy
            non-prime positions. The answer is the product of factorials of each group.

        Approach:
            Use Sieve of Eratosthenes to count primes up to n. The result is
            factorial(prime_count) * factorial(n - prime_count) modulo 10^9 + 7.

        Complexity:
            Time: O(n log log n)
            Space: O(n)
        """
        MOD = 10**9 + 7

        def count_primes(limit: int) -> int:
            is_prime = [True] * (limit + 1)
            prime_count = 0
            for i in range(2, limit + 1):
                if is_prime[i]:
                    prime_count += 1
                    for j in range(i + i, limit + 1, i):
                        is_prime[j] = False
            return prime_count

        prime_count = count_primes(n)
        return (factorial(prime_count) * factorial(n - prime_count)) % MOD
