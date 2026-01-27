class Solution:
    def beautifulArray(self, n: int) -> list[int]:
        """Divide and conquer separating odd and even indexed elements.

        Intuition:
            A beautiful array has no arithmetic triple. By placing odd-indexed
            elements on the left and even-indexed on the right, any triple
            spanning both halves cannot be arithmetic since left values are
            odd and right values are even.

        Approach:
            1. Base case: n=1 returns [1].
            2. Recursively build beautiful arrays for ceil(n/2) and floor(n/2).
            3. Map left array to odd positions (2x-1) and right to even (2x).
            4. Concatenate the two halves.

        Complexity:
            Time: O(n log n)
            Space: O(n log n)
        """
        if n == 1:
            return [1]
        odd_half = self.beautifulArray((n + 1) >> 1)
        even_half = self.beautifulArray(n >> 1)
        odd_values = [x * 2 - 1 for x in odd_half]
        even_values = [x * 2 for x in even_half]
        return odd_values + even_values
