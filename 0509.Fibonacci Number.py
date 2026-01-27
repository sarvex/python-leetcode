class Solution:
    def fib(self, n: int) -> int:
        """Iterative Fibonacci using two variables.

        Intuition:
            Each Fibonacci number is the sum of the previous two. We only
            need to track the last two values.

        Approach:
            Initialize two variables for F(0) and F(1), then iterate n times,
            updating both values each step.

        Complexity:
            Time: O(n)
            Space: O(1)
        """
        prev, curr = 0, 1
        for _ in range(n):
            prev, curr = curr, prev + curr
        return prev
