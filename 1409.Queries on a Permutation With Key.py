class Solution:
    def processQueries(self, queries: list[int], m: int) -> list[int]:
        """Process queries on a permutation, moving queried elements to front.

        Intuition:
            Simulate the process: find the position of each query value,
            record it, then move the value to the front.

        Approach:
            Maintain a list representing the permutation. For each query,
            find the index, record it, remove the element, and insert it
            at position 0.

        Complexity:
            Time: O(q * m) where q is number of queries
            Space: O(m) for the permutation list
        """
        permutation = list(range(1, m + 1))
        result: list[int] = []
        for value in queries:
            position = permutation.index(value)
            result.append(position)
            permutation.pop(position)
            permutation.insert(0, value)
        return result
