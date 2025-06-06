class Solution:
    def tribonacci(self, n: int) -> int:
        """Dynamic Programming with constant space

        Intuition:
        The Tribonacci sequence is similar to Fibonacci but uses the sum of the last three
        numbers instead of two. We can compute it iteratively using three variables.

        Approach:
        Use three variables to keep track of the last three Tribonacci numbers.
        In each iteration, shift the values and compute the next number in the sequence.

        Complexity:
        Time: O(n) where n is the input parameter
        Space: O(1) as we only use three variables regardless of input size
        """
        # Handle base cases efficiently
        if n == 0:
            return 0
        if n <= 2:
            return 1

        # Initialize the first three numbers in the sequence
        a, b, c = 0, 1, 1

        # Calculate the nth Tribonacci number iteratively
        for _ in range(n - 2):
            a, b, c = b, c, a + b + c
        return c
