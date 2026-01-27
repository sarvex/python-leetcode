class Solution:
    def minSwapsCouples(self, row: list[int]) -> int:
        """Union-Find to count disjoint couple cycles.

        Intuition:
            Each pair of adjacent seats should hold a couple. Model each couple
            as a node; union the couples sitting in adjacent seats. The number
            of swaps equals N minus the number of connected components.

        Approach:
            1. Create a Union-Find with N = len(row)/2 elements (one per couple).
            2. For each pair of adjacent seats, union the two couple-ids.
            3. Count roots; answer is N - number_of_components.

        Complexity:
            Time: O(N * α(N))
            Space: O(N)
        """

        def find(x: int) -> int:
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        num_couples = len(row) >> 1
        parent = list(range(num_couples))
        for i in range(0, len(row), 2):
            couple_a, couple_b = row[i] >> 1, row[i + 1] >> 1
            parent[find(couple_a)] = find(couple_b)
        return num_couples - sum(i == find(i) for i in range(num_couples))
