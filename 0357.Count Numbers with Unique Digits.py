class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        """Count numbers with unique digits using combinatorial counting.

        Intuition:
            For n digits, the count of numbers with unique digits can be built
            incrementally. Each additional digit position has fewer available
            choices since digits cannot repeat.

        Approach:
            Base cases handle n=0 (only 0) and n=1 (0-9). For n>=2, multiply
            the available digit choices for each position: first digit has 9
            choices (1-9), second has 9 (0-9 minus first), third has 8, etc.
            Accumulate the count for each digit length.

        Complexity:
            Time: O(n)
            Space: O(1)
        """
        if n == 0:
            return 1
        if n == 1:
            return 10
        total, current = 10, 9
        for i in range(n - 1):
            current *= 9 - i
            total += current
        return total
