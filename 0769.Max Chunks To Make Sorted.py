class Solution:
    def maxChunksToSorted(self, arr: list[int]) -> int:
        """Track running maximum and count when it equals the index.

        Intuition:
            Since arr is a permutation of [0, n-1], a chunk [0..i] is valid when
            the maximum value seen so far equals i, meaning all values 0..i are
            contained in that prefix.

        Approach:
            1. Iterate through the array tracking the running maximum
            2. Whenever the running maximum equals the current index, increment
               the chunk count
            3. Return the total chunk count

        Complexity:
            Time: O(n)
            Space: O(1)
        """
        current_max = chunks = 0
        for i, value in enumerate(arr):
            current_max = max(current_max, value)
            if i == current_max:
                chunks += 1
        return chunks
