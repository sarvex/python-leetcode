from functools import lru_cache


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """Dynamic programming approach to find minimum edit distance between two strings.

        Intuition:
            The edit distance problem can be solved by considering the operations needed
            to transform one string into another. At each step, we have three possible
            operations: insert, delete, or replace a character.

        Approach:
            Use a 2D DP table where dp[i][j] represents the minimum number of operations
            required to convert word1[0...i-1] to word2[0...j-1].
            - Base cases:
              - dp[i][0] = i (delete i characters from word1)
              - dp[0][j] = j (insert j characters from word2)
            - For each character pair:
              - If characters match: dp[i][j] = dp[i-1][j-1] (no operation needed)
              - If characters differ: dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
                representing delete, insert, and replace operations respectively.

        Complexity:
            Time: O(m*n) where m and n are lengths of word1 and word2
            Space: O(m*n) for the DP table
        """
        m, n = len(word1), len(word2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # Base cases
        for j in range(1, n + 1):
            dp[0][j] = j

        for i, char1 in enumerate(word1, 1):
            dp[i][0] = i
            for j, char2 in enumerate(word2, 1):
                if char1 == char2:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(
                        dp[i - 1][j],    # Delete
                        dp[i][j - 1],    # Insert
                        dp[i - 1][j - 1] # Replace
                    )

        return dp[m][n]

    def minDistance_optimized(self, word1: str, word2: str) -> int:
        """Space-optimized dynamic programming solution for edit distance.

        Intuition:
            We can optimize the space complexity by using only two rows of the DP table
            since we only need the current and previous row for calculations.

        Approach:
            Use two 1D arrays (prev and curr) to store the previous and current rows of
            the DP table. After processing each row, prev becomes curr and we reset curr.

        Complexity:
            Time: O(m*n) where m and n are lengths of word1 and word2
            Space: O(min(m,n)) using only two rows of the DP table
        """
        # Ensure word1 is the shorter string for space optimization
        if len(word1) > len(word2):
            word1, word2 = word2, word1

        m, n = len(word1), len(word2)
        prev_row = list(range(n + 1))  # Initialize first row with [0,1,2,...,n]

        for i in range(1, m + 1):
            curr_row = [i] + [0] * n  # Initialize current row with [i,0,0,...,0]

            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    curr_row[j] = prev_row[j - 1]
                else:
                    curr_row[j] = 1 + min(
                        prev_row[j],     # Delete
                        curr_row[j - 1], # Insert
                        prev_row[j - 1]  # Replace
                    )

            prev_row = curr_row

        return prev_row[n]

    def minDistance_recursive(self, word1: str, word2: str) -> int:
        """Recursive solution with memoization for edit distance.

        Intuition:
            We can solve this problem recursively by considering all possible operations
            at each step and choosing the minimum cost path. Memoization prevents
            redundant calculations.

        Approach:
            Use a recursive function with memoization that computes the edit distance
            between word1[0...i] and word2[0...j]. At each step:
            - If characters match, no operation needed
            - Otherwise, try all three operations (insert, delete, replace) and take minimum

        Complexity:
            Time: O(m*n) where m and n are lengths of word1 and word2
            Space: O(m*n) for the memoization cache and recursion stack
        """
        memo = {}

        def edit_distance(i: int, j: int) -> int:
            """Calculate edit distance between word1[0...i] and word2[0...j]."""
            # Base cases
            if i == 0:
                return j  # Insert j characters
            if j == 0:
                return i  # Delete i characters

            # Check if already computed
            if (i, j) in memo:
                return memo[(i, j)]

            # If characters match, no operation needed
            if word1[i-1] == word2[j-1]:
                result = edit_distance(i-1, j-1)
            else:
                # Try all three operations and take minimum
                delete_op = edit_distance(i-1, j)      # Delete from word1
                insert_op = edit_distance(i, j-1)      # Insert into word1
                replace_op = edit_distance(i-1, j-1)   # Replace in word1
                result = 1 + min(delete_op, insert_op, replace_op)

            # Memoize and return
            memo[(i, j)] = result
            return result

        return edit_distance(len(word1), len(word2))

    def minDistance_concise(self, word1: str, word2: str) -> int:
        """Concise recursive solution using Python's lru_cache decorator.

        Intuition:
            Same as the recursive approach, but using Python's built-in memoization.

        Approach:
            Use @lru_cache decorator to automatically handle memoization of recursive calls.
            This creates a cleaner implementation while maintaining the same logic.

        Complexity:
            Time: O(m*n) where m and n are lengths of word1 and word2
            Space: O(m*n) for the memoization cache and recursion stack
        """
        @lru_cache(maxsize=None)
        def edit_distance(i: int, j: int) -> int:
            """Calculate edit distance between word1[0...i] and word2[0...j]."""
            # Base cases
            if i == 0:
                return j  # Insert j characters
            if j == 0:
                return i  # Delete i characters

            # If characters match, no operation needed
            if word1[i-1] == word2[j-1]:
                return edit_distance(i-1, j-1)

            # Try all three operations and take minimum
            delete_op = edit_distance(i-1, j)      # Delete from word1
            insert_op = edit_distance(i, j-1)      # Insert into word1
            replace_op = edit_distance(i-1, j-1)   # Replace in word1
            return 1 + min(delete_op, insert_op, replace_op)

        return edit_distance(len(word1), len(word2))
