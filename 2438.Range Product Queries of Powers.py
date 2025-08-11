from typing import List

MOD = 10**9 + 7


class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        """
        Compute range product queries on powers of 2 representation of n.
        
        Intuition:
        First thoughts on solving this problem - we need to decompose n into powers of 2,
        then for each query range [left, right], compute the product of powers in that range.
        
        Approach:
        1. Extract all powers of 2 from n using bit manipulation (n & -n gives lowest set bit)
        2. Build a 2D prefix product matrix where matrix[i][j] = product from index i to j
        3. Answer each query using the precomputed matrix
        
        Complexity:
        Time: O(k^2 + q) where k is number of set bits in n, q is number of queries
        Space: O(k^2) for the prefix product matrix
        """
        # Extract all powers of 2 from n
        powers = []
        while n:
            lowest_bit = n & -n
            powers.append(lowest_bit)
            n ^= lowest_bit
        
        # Build 2D prefix product matrix
        size = len(powers)
        prefix_matrix = [[0] * size for _ in range(size)]
        
        for i, power in enumerate(powers):
            prefix_matrix[i][i] = power
            for j in range(i + 1, size):
                prefix_matrix[i][j] = (prefix_matrix[i][j - 1] * powers[j]) % MOD
        
        return [prefix_matrix[left][right] for left, right in queries]