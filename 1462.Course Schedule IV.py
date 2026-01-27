class Solution:
    def checkIfPrerequisite(
        self, n: int, prerequisites: list[list[int]], queries: list[list[int]]
    ) -> list[bool]:
        """Answer prerequisite queries using Floyd-Warshall transitive closure.

        Intuition:
            Precompute the full reachability matrix so each query is O(1).

        Approach:
            Initialize a boolean matrix from direct prerequisites. Apply
            Floyd-Warshall to compute transitive closure: if course i reaches
            k and k reaches j, then i reaches j.

        Complexity:
            Time: O(n^3) for Floyd-Warshall
            Space: O(n^2) for the reachability matrix
        """
        is_prerequisite = [[False] * n for _ in range(n)]
        for source, target in prerequisites:
            is_prerequisite[source][target] = True
        for intermediate in range(n):
            for source in range(n):
                for target in range(n):
                    if (
                        is_prerequisite[source][intermediate]
                        and is_prerequisite[intermediate][target]
                    ):
                        is_prerequisite[source][target] = True
        return [is_prerequisite[source][target] for source, target in queries]
