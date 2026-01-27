class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        """Find minimum Fibonacci numbers that sum to k.

        Intuition:
            Greedily subtract the largest Fibonacci number not exceeding k.
            This greedy approach works due to Zeckendorf's theorem.

        Approach:
            Recursively find the largest Fibonacci number <= k, subtract it,
            and count. Base case: k < 2 returns k itself.

        Complexity:
            Time: O(log(k)^2) generating Fibonacci numbers per recursion
            Space: O(log(k)) recursion depth
        """

        def count_fibonacci(remaining: int) -> int:
            if remaining < 2:
                return remaining
            previous, current = 1, 1
            while current <= remaining:
                previous, current = current, previous + current
            return 1 + count_fibonacci(remaining - previous)

        return count_fibonacci(k)
