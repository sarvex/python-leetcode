class Solution:
    def isHappy(self, n: int) -> bool:
        """Detect happy number using a visited set for cycle detection.

        Intuition:
            Repeatedly replacing a number by the sum of squares of its digits
            either reaches 1 or enters a cycle. Tracking visited numbers
            detects the cycle.

        Approach:
            1. Maintain a set of previously seen numbers.
            2. Compute the sum of squared digits for the current number.
            3. If the result is 1, return True. If already seen, return False.

        Complexity:
            Time: O(log n) per step, bounded number of steps
            Space: O(log n) for the visited set
        """
        visited = set()
        while n != 1 and n not in visited:
            visited.add(n)
            digit_square_sum = 0
            while n:
                n, digit = divmod(n, 10)
                digit_square_sum += digit * digit
            n = digit_square_sum
        return n == 1
