from collections import Counter


class Solution:
    def countLargestGroup(self, n: int) -> int:
        """Count groups with the largest size based on digit sum grouping.

        Intuition:
            Group numbers 1..n by their digit sum. Count how many groups
            share the maximum group size.

        Approach:
            For each number, compute its digit sum and track group sizes
            using a counter. Maintain the current maximum and count of
            groups achieving that maximum.

        Complexity:
            Time: O(n * d) where d is the number of digits
            Space: O(n) for the counter
        """
        digit_sum_count: Counter[int] = Counter()
        result = max_size = 0
        for number in range(1, n + 1):
            digit_sum = 0
            temp = number
            while temp:
                digit_sum += temp % 10
                temp //= 10
            digit_sum_count[digit_sum] += 1
            if max_size < digit_sum_count[digit_sum]:
                max_size = digit_sum_count[digit_sum]
                result = 1
            elif max_size == digit_sum_count[digit_sum]:
                result += 1
        return result
