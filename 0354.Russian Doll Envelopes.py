from bisect import bisect_left


class Solution:
    def maxEnvelopes(self, envelopes: list[list[int]]) -> int:
        """Sort + LIS via patience sorting for Russian doll envelopes.

        Intuition:
            Sort by width ascending and height descending so that the problem
            reduces to finding the longest increasing subsequence on heights.

        Approach:
            1. Sort envelopes by width ascending; break ties with height
               descending to avoid using two envelopes with the same width.
            2. Apply the O(n log n) LIS algorithm using binary search on
               the heights.

        Complexity:
            Time: O(n log n)
            Space: O(n)
        """
        envelopes.sort(key=lambda envelope: (envelope[0], -envelope[1]))
        tails = [envelopes[0][1]]
        for _, height in envelopes[1:]:
            if height > tails[-1]:
                tails.append(height)
            else:
                idx = bisect_left(tails, height)
                if idx == len(tails):
                    idx = 0
                tails[idx] = height
        return len(tails)
