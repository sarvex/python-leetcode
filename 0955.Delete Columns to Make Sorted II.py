from typing import List


class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        """
        Return the minimum number of columns to delete such that the remaining strings
        are in lexicographical order.

        Intuition:
        We process the strings column by column. A column is kept if it doesn't break
        the lexicographical order for any pair of adjacent strings that aren't already
        strictly sorted by previous columns.

        Approach:
        1. Initialize `is_sorted` boolean array of size n-1, all False.
           `is_sorted[i]` is True if `strs[i] < strs[i+1]` is already guaranteed by previous columns.
        2. Iterate through each column index `j`:
           a. Check if any adjacent pair `(i, i+1)` has `strs[i][j] > strs[i+1][j]` while `is_sorted[i]` is False.
           b. If such a pair exists, this column MUST be deleted. Increment answer.
           c. If no such pair exists, the column is kept. Update `is_sorted[i]` to True
              if `strs[i][j] < strs[i+1][j]`.
        3. Return the count of deleted columns.

        Complexity:
        Time: O(n * m), where n is the number of strings and m is the length of each string.
        Space: O(n) to store the `is_sorted` array.
        """
        n = len(strs)
        if n <= 1:
            return 0

        m = len(strs[0])
        ans = 0
        # is_sorted[i] = True if strs[i] < strs[i+1] is already determined
        is_sorted = [False] * (n - 1)

        for j in range(m):
            should_delete = False
            for i in range(n - 1):
                if not is_sorted[i] and strs[i][j] > strs[i + 1][j]:
                    should_delete = True
                    break

            if should_delete:
                ans += 1
            else:
                # Keep the column and update sorted state
                for i in range(n - 1):
                    if not is_sorted[i] and strs[i][j] < strs[i + 1][j]:
                        is_sorted[i] = True

        return ans
