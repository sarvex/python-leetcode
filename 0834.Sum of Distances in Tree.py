from collections import defaultdict


class Solution:
    def sumOfDistancesInTree(self, n: int, edges: list[list[int]]) -> list[int]:
        """Two-pass DFS for rerooting technique on tree distances.

        Intuition:
            Compute the answer for root 0, then reroot to each child using
            the relationship: moving the root from parent to child decreases
            distance for child's subtree and increases for the rest.

        Approach:
            1. First DFS: compute subtree sizes and total distance from root 0.
            2. Second DFS: for each child, adjust the parent's answer using
               ans[child] = ans[parent] - subtree_size[child] + (n - subtree_size[child]).

        Complexity:
            Time: O(n)
            Space: O(n)
        """

        def compute_sizes(node: int, parent: int, depth: int) -> None:
            distances[0] += depth
            subtree_size[node] = 1
            for neighbor in adjacency[node]:
                if neighbor != parent:
                    compute_sizes(neighbor, node, depth + 1)
                    subtree_size[node] += subtree_size[neighbor]

        def reroot(node: int, parent: int, current_dist: int) -> None:
            distances[node] = current_dist
            for neighbor in adjacency[node]:
                if neighbor != parent:
                    reroot(
                        neighbor,
                        node,
                        current_dist
                        - subtree_size[neighbor]
                        + n
                        - subtree_size[neighbor],
                    )

        adjacency: defaultdict[int, list[int]] = defaultdict(list)
        for node_a, node_b in edges:
            adjacency[node_a].append(node_b)
            adjacency[node_b].append(node_a)

        distances = [0] * n
        subtree_size = [0] * n
        compute_sizes(0, -1, 0)
        reroot(0, -1, distances[0])
        return distances
