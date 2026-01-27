class Solution:
    def earliestAcq(self, logs: list[list[int]], n: int) -> int:
        """Find earliest time all people are connected using Union-Find.

        Intuition:
            This is a dynamic connectivity problem. Process friendship events
            in chronological order and use Union-Find to track connected
            components until everyone is in a single component.

        Approach:
            Sort logs by timestamp. Use Union-Find with path compression.
            For each log, union the two people. Decrement component count
            on each successful union. Return the timestamp when components
            reach 1.

        Complexity:
            Time: O(m log m + m * α(n)) where m is number of logs
            Space: O(n) for the parent array
        """

        def find(x: int) -> int:
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        parent = list(range(n))
        components = n
        for timestamp, person_a, person_b in sorted(logs):
            root_a, root_b = find(person_a), find(person_b)
            if root_a == root_b:
                continue
            parent[root_a] = root_b
            components -= 1
            if components == 1:
                return timestamp
        return -1
