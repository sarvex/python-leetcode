from collections import deque
from itertools import pairwise


class Solution:
    def sequenceReconstruction(
        self, nums: list[int], sequences: list[list[int]]
    ) -> bool:
        """Topological sort verifying a unique reconstruction from subsequences.

        Intuition:
            The original sequence can be uniquely reconstructed if and only if
            the topological sort has exactly one valid ordering, meaning the
            queue never has more than one element at any step.

        Approach:
            1. Build a directed graph from consecutive pairs in each subsequence.
            2. Compute in-degrees for all nodes.
            3. Perform BFS topological sort; at each step ensure only one node
               has in-degree 0 (queue size == 1).
            4. If the queue ever has more than one element, return False.
               If all nodes are processed, return True.

        Complexity:
            Time: O(V + E) where V is the number of elements and E is total pairs.
            Space: O(V + E) for the graph and in-degree array.
        """
        num_elements = len(nums)
        graph: list[list[int]] = [[] for _ in range(num_elements)]
        in_degree = [0] * num_elements
        for sequence in sequences:
            for source, target in pairwise(sequence):
                source, target = source - 1, target - 1
                graph[source].append(target)
                in_degree[target] += 1
        queue = deque(i for i, degree in enumerate(in_degree) if degree == 0)
        while len(queue) == 1:
            node = queue.popleft()
            for neighbor in graph[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        return len(queue) == 0
