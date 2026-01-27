class Solution:
    def integerReplacement(self, n: int) -> int:
        """Greedy bit manipulation to minimize steps to reach 1.

        Intuition:
            For even numbers, divide by 2. For odd numbers, choose +1 or -1
            based on which eliminates more trailing bits. The special case
            n=3 prefers -1 since 3->2->1 is shorter than 3->4->2->1.

        Approach:
            1. If n is even, right-shift (divide by 2).
            2. If n is odd and n != 3 and last two bits are 11, increment.
            3. Otherwise, decrement.
            4. Count steps until n becomes 1.

        Complexity:
            Time: O(log n)
            Space: O(1)
        """
        steps = 0
        while n != 1:
            if (n & 1) == 0:
                n >>= 1
            elif n != 3 and (n & 3) == 3:
                n += 1
            else:
                n -= 1
            steps += 1
        return steps
