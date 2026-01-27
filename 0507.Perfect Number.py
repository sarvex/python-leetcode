class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        """Check if a number equals the sum of its proper divisors.

        Intuition:
            A perfect number equals the sum of its proper divisors. We only
            need to check divisors up to sqrt(num) and add both divisor pairs.

        Approach:
            Start with divisor_sum = 1 (every number > 1 has 1 as divisor).
            Iterate from 2 to sqrt(num), adding both i and num/i when divisible.

        Complexity:
            Time: O(sqrt(num))
            Space: O(1)
        """
        if num == 1:
            return False
        divisor_sum, divisor = 1, 2
        while divisor * divisor <= num:
            if num % divisor == 0:
                divisor_sum += divisor
                if divisor != num // divisor:
                    divisor_sum += num // divisor
            divisor += 1
        return divisor_sum == num
