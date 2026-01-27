from collections import Counter


class UnionFind:
    def __init__(self, size: int) -> None:
        self.parent = list(range(size))

    def union(self, a: int, b: int) -> None:
        root_a, root_b = self.find(a), self.find(b)
        if root_a != root_b:
            self.parent[root_a] = root_b

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]


class Solution:
    def largestComponentSize(self, nums: list[int]) -> int:
        """Union-Find grouping numbers by shared prime factors.

        Intuition:
            Two numbers are connected if they share a common factor > 1.
            Union each number with all its prime factors to build components.

        Approach:
            1. Create Union-Find with size max(nums) + 1.
            2. For each number, find all factors and union the number with each factor.
            3. Count component sizes by finding roots for all numbers in the input.
            4. Return the largest component size.

        Complexity:
            Time: O(n * sqrt(m)) — factor finding for each number, m = max(nums)
            Space: O(m) — Union-Find parent array
        """
        uf = UnionFind(max(nums) + 1)
        for value in nums:
            factor = 2
            while factor <= value // factor:
                if value % factor == 0:
                    uf.union(value, factor)
                    uf.union(value, value // factor)
                factor += 1
        return max(Counter(uf.find(value) for value in nums).values())
