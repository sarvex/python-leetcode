class Solution:
    def climbStairs(self, n: int) -> int:
        """Fibonacci Dynamic Programming Approach

        Intuition:
            The number of ways to reach step n equals the sum of ways to
            reach step n-1 and step n-2, forming the Fibonacci sequence.

        Approach:
            Iterate from 1 to n, maintaining two variables that track the
            previous two Fibonacci values. At each step, update them by
            shifting forward.

        Complexity:
            Time: O(n)
            Space: O(1)
        """
        prev, curr = 0, 1
        for _ in range(n):
            prev, curr = curr, prev + curr
        return curr
