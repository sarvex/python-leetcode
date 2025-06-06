from typing import List
from collections import defaultdict


class Solution:
    def calcEquation(
        self, equations: List[List[str]], values: List[float], queries: List[List[str]]
    ) -> List[float]:
        """Union-Find with weights to evaluate division equations and queries.

        Intuition:
            Represent the division relationships as a weighted graph where each variable is a node,
            and the weight of an edge represents the division result. Use Union-Find with weights
            to efficiently track relationships and compute query results.

        Approach:
            1. Initialize each variable as its own parent with weight 1
            2. Union variables in equations with their respective values
            3. For each query, check if both variables exist and have the same parent
            4. If they do, return the ratio of their weights; otherwise, return -1

        Complexity:
            Time: O(N + Q), where N is the number of equations and Q is the number of queries
            Space: O(V), where V is the number of unique variables
        """
        def find(x: str) -> str:
            """Find the root parent of x and update weights along the path."""
            if parents[x] != x:
                origin = parents[x]
                parents[x] = find(parents[x])
                weights[x] *= weights[origin]
            return parents[x]

        # Initialize weight and parent dictionaries
        weights = defaultdict(lambda: 1)
        parents = {}

        # Initialize each variable as its own parent
        for a, b in equations:
            parents[a], parents[b] = a, b

        # Union variables based on equations
        for i, v in enumerate(values):
            a, b = equations[i]
            pa, pb = find(a), find(b)
            if pa == pb:
                continue
            parents[pa] = pb
            weights[pa] = weights[b] * v / weights[a]

        # Process queries
        return [
            -1 if c not in parents or d not in parents or find(c) != find(d) else weights[c] / weights[d]
            for c, d in queries
        ]
