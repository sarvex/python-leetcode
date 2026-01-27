class Solution:
    def findJudge(self, n: int, trust: list[list[int]]) -> int:
        """Find the town judge who trusts nobody and is trusted by everyone else.

        Intuition:
            The judge has in-degree n-1 and out-degree 0 in the trust graph.
            Track both counts per person.

        Approach:
            Count outgoing trusts and incoming trusts separately. The judge is
            the person with zero outgoing and n-1 incoming trust edges.

        Complexity:
            Time: O(n + t) where t is the number of trust pairs
            Space: O(n) for the two count arrays
        """
        trusts_others = [0] * (n + 1)
        trusted_by = [0] * (n + 1)
        for source, target in trust:
            trusts_others[source] += 1
            trusted_by[target] += 1
        for person in range(1, n + 1):
            if trusts_others[person] == 0 and trusted_by[person] == n - 1:
                return person
        return -1
