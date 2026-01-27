class Solution:
    def minHeightShelves(self, books: list[list[int]], shelfWidth: int) -> int:
        """Minimize bookshelf height using dynamic programming.

        Intuition:
            For each book, decide whether to start a new shelf or place it on
            the current shelf. DP lets us try all valid groupings and pick the
            one with minimum total height.

        Approach:
            Define f[i] as the minimum height for the first i books. For each
            book i, try placing books i, i-1, ... on the same shelf as long as
            the total width does not exceed shelfWidth, tracking the maximum
            height on that shelf.

        Complexity:
            Time: O(n * w) where n is number of books and w is books per shelf
            Space: O(n) for the DP array
        """
        num_books = len(books)
        dp = [0] * (num_books + 1)
        for i, (width, height) in enumerate(books, 1):
            dp[i] = dp[i - 1] + height
            for j in range(i - 1, 0, -1):
                width += books[j - 1][0]
                if width > shelfWidth:
                    break
                height = max(height, books[j - 1][1])
                dp[i] = min(dp[i], dp[j - 1] + height)
        return dp[num_books]
