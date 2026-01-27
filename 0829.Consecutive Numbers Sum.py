class Solution:
    def consecutiveNumbersSum(self, n: int) -> int:
        """Count ways to express n as sum of consecutive positive integers.

        Intuition:
            A sequence of k consecutive numbers starting at a has sum
            k*a + k*(k-1)/2 = n. So 2n = k*(2a + k - 1), meaning k must
            divide 2n and the quotient must have correct parity.

        Approach:
            1. Double n to avoid fractions.
            2. Iterate k from 1 while k*(k+1) <= 2n.
            3. Check if 2n is divisible by k and (2n/k - k + 1) is even and positive.

        Complexity:
            Time: O(sqrt(n))
            Space: O(1)
        """
        doubled = n << 1
        count, length = 0, 1
        while length * (length + 1) <= doubled:
            if doubled % length == 0 and (doubled // length - length + 1) % 2 == 0:
                count += 1
            length += 1
        return count
