class Solution:
    def longestDecomposition(self, text: str) -> int:
        """Find the largest k for chunked palindrome decomposition.

        Intuition:
            Greedily match the shortest prefix with the corresponding suffix
            to maximize the number of chunks.

        Approach:
            Compare prefixes and suffixes of increasing length. When a match
            is found, count 2 chunks and recurse on the remaining middle
            portion. Base case: empty string yields 0, single-char yields 1.

        Complexity:
            Time: O(n^2) where n is the length of text due to string comparison
            Space: O(n) for recursion stack
        """
        length = len(text)
        if length < 2:
            return length
        for i in range(1, length // 2 + 1):
            if text[:i] == text[-i:]:
                return 2 + self.longestDecomposition(text[i:-i])
        return 1
