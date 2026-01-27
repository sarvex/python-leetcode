class Solution:
    def sumFourDivisors(self, nums: list[int]) -> int:
        """Sum of divisors for numbers with exactly four divisors.

        Intuition:
            For each number, count its divisors by iterating up to sqrt.
            If a number has exactly four divisors, add their sum.

        Approach:
            For each number, iterate from 2 to sqrt(x) to find divisor pairs.
            Track divisor count and sum. Return the sum only when count is 4.

        Complexity:
            Time: O(n * sqrt(max_val)) for checking each number
            Space: O(1) auxiliary space
        """

        def divisor_sum_if_four(x: int) -> int:
            divisor = 2
            count, total = 2, x + 1
            while divisor <= x // divisor:
                if x % divisor == 0:
                    count += 1
                    total += divisor
                    if divisor * divisor != x:
                        count += 1
                        total += x // divisor
                divisor += 1
            return total if count == 4 else 0

        return sum(divisor_sum_if_four(x) for x in nums)
