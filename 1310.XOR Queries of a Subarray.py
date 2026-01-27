from itertools import accumulate
from operator import xor


class Solution:
    def xorQueries(self, arr: list[int], queries: list[list[int]]) -> list[int]:
        """Answer XOR queries on subarrays using prefix XOR.

        Intuition:
            XOR is its own inverse, so the XOR of a subarray can be computed from
            a prefix XOR array in O(1) per query.

        Approach:
            Build a prefix XOR array with an initial 0. For each query [left, right],
            the answer is prefix[right+1] ^ prefix[left].

        Complexity:
            Time: O(n + q) where q is the number of queries
            Space: O(n)
        """
        prefix_xor = list(accumulate(arr, xor, initial=0))
        return [prefix_xor[right + 1] ^ prefix_xor[left] for left, right in queries]
