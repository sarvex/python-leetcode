class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        """Prefix scan counting zeros to find optimal split point.

        Intuition:
            At each position, the cost of making the string monotone increasing
            is: flipping 1s to 0s on the left + flipping 0s to 1s on the right.
            We can track this with a running count of zeros.

        Approach:
            1. Count total zeros (cost of flipping all zeros to ones).
            2. Scan left to right, tracking zeros seen so far.
            3. At each position i, the cost is (ones on left) + (zeros on right)
               = (i - zeros_seen) + (total_zeros - zeros_seen).
            4. Return the minimum cost.

        Complexity:
            Time: O(n)
            Space: O(1)
        """
        total_zeros = s.count("0")
        result, zeros_seen = total_zeros, 0
        for idx, char in enumerate(s, 1):
            zeros_seen += int(char == "0")
            result = min(result, idx - zeros_seen + total_zeros - zeros_seen)
        return result
