class Solution:
    def numDupDigitsAtMostN(self, n: int) -> int:
        """Count numbers up to n that have at least one repeated digit.

        Intuition:
            It is easier to count numbers with all unique digits and subtract
            from n. Use digit DP counting approach.

        Approach:
            Count numbers with all distinct digits up to n. For numbers with
            fewer digits, use permutation counts. For numbers with the same
            digit count, iterate digit by digit tracking used digits.

        Complexity:
            Time: O(log(n) * 10) for digit-by-digit processing
            Space: O(log n) for the digit array
        """
        return n - self._count_unique(n)

    def _count_unique(self, n: int) -> int:
        def permutations(total: int, choose: int) -> int:
            if choose == 0:
                return 1
            return permutations(total, choose - 1) * (total - choose + 1)

        used = [False] * 10
        count = 0
        digits = [int(ch) for ch in str(n)[::-1]]
        num_digits = len(digits)
        for length in range(1, num_digits):
            count += 9 * permutations(9, length - 1)
        for i in range(num_digits - 1, -1, -1):
            digit = digits[i]
            start = 1 if i == num_digits - 1 else 0
            for candidate in range(start, digit):
                if not used[candidate]:
                    count += permutations(10 - (num_digits - i), i)
            if used[digit]:
                break
            used[digit] = True
            if i == 0:
                count += 1
        return count
