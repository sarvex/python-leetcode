class Solution:
    def countPrimes(self, n: int) -> int:
        """Sieve of Eratosthenes to count primes less than n.

        Intuition:
            Mark all multiples of each prime as composite. The remaining
            unmarked numbers are prime.

        Approach:
            1. Create a boolean array of size n, initialized to True.
            2. For each number from 2 to n-1, if still marked prime, increment
               count and mark all its multiples as not prime.

        Complexity:
            Time: O(n log log n)
            Space: O(n)
        """
        is_prime = [True] * n
        count = 0
        for i in range(2, n):
            if is_prime[i]:
                count += 1
                for j in range(i + i, n, i):
                    is_prime[j] = False
        return count
