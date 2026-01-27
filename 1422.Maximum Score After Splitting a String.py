class Solution:
    def maxScore(self, s: str) -> int:
        """Find maximum score from splitting string into zeros-left + ones-right.

        Intuition:
            Try every valid split point and count zeros in the left part
            plus ones in the right part.

        Approach:
            For each split index from 1 to len-1, count '0's in the left
            substring and '1's in the right substring. Return the maximum.

        Complexity:
            Time: O(n^2) due to counting at each split point
            Space: O(n) for string slicing
        """
        return max(s[:i].count("0") + s[i:].count("1") for i in range(1, len(s)))
