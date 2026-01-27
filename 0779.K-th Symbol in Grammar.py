class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        """Recursive halving based on the binary tree structure of the grammar.

        Intuition:
            Each row is generated from the previous: 0 becomes 01, 1 becomes 10.
            The k-th element in row n depends on whether k is in the first or
            second half of the row, with the second half being flipped.

        Approach:
            1. Base case: row 1 always has value 0
            2. If k is in the first half of row n, it equals the k-th element of row n-1
            3. If k is in the second half, it equals the flipped value of the
               corresponding element in the first half

        Complexity:
            Time: O(n) recursive calls
            Space: O(n) for recursion stack
        """
        if n == 1:
            return 0
        half = 1 << (n - 2)
        if k <= half:
            return self.kthGrammar(n - 1, k)
        return self.kthGrammar(n - 1, k - half) ^ 1
