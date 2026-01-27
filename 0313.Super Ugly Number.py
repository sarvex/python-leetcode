from heapq import heappop, heappush


class Solution:
    def nthSuperUglyNumber(self, n: int, primes: list[int]) -> int:
        """Min-heap approach generating super ugly numbers in order.

        Intuition:
            Use a min-heap to always extract the smallest super ugly number,
            then generate new candidates by multiplying with each prime.

        Approach:
            1. Start with 1 in the heap.
            2. Pop the smallest value n times.
            3. For each popped value, multiply by each prime and push the
               product. Stop multiplying further primes if the value is
               divisible by the current prime (avoids duplicates).

        Complexity:
            Time: O(n * k * log(n*k)) where k is the number of primes
            Space: O(n * k) for the heap
        """
        heap = [1]
        current = 0
        max_val = (1 << 31) - 1
        for _ in range(n):
            current = heappop(heap)
            for prime in primes:
                if current <= max_val // prime:
                    heappush(heap, prime * current)
                if current % prime == 0:
                    break
        return current
