class Solution:
    def kthCharacter(self, k: int) -> str:
        """
        Binary pattern recognition approach

        Intuition:
        The sequence follows a pattern where each new sequence is derived from the previous
        one with a transformation. Instead of generating the entire sequence, we can
        determine the kth character using binary representation properties.

        Approach:
        1. Observe that the sequence follows a pattern where each element is (previous + 1) % 26
        2. Use binary representation to find the exact character without generating the full sequence
        3. Calculate the pattern directly for the kth position

        Complexity:
        Time: O(log k) - We need log k operations to determine the character
        Space: O(1) - Constant extra space used
        """
        # Find the minimum power of 2 that exceeds k
        n = 1
        while n < k:
            n *= 2

        # Adjust k to be relative to the current sequence
        k -= 1

        # Calculate the character at position k
        result = 0
        while k > 0:
            # Reduce to previous sequence and adjust the value
            n //= 2
            if k >= n:
                k -= n
                result = (result + 1) % 26

        return chr(ord('a') + result)
