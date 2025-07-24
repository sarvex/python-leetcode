from typing import List


class Solution:
    def minimumScore(self, nums: List[int], edges: List[List[int]]) -> int:
        """
        Optimized tree partitioning using iterative DFS with in/out time tracking

        Intuition:
        Use DFS to precompute subtree XOR values and track parent-child relationships
        with in/out times. This allows O(1) ancestor checking for efficient edge removal.

        Approach:
        1. Build adjacency list and perform iterative DFS to compute:
           - Subtree XOR values for each node
           - Parent relationships
           - In/out times for ancestor checking
        2. Try all pairs of nodes as edge removals
        3. Use in/out times to determine tree structure after removals
        4. Calculate three component XOR values and track minimum score

        Complexity:
        Time: O(n²) - trying all node pairs with O(1) calculations
        Space: O(n) - adjacency list and tracking arrays
        """
        n = len(nums)
        adjacency_list = self._build_adjacency_list(edges, n)

        # Precompute tree properties using iterative DFS
        subtree_xor, parent, in_time, out_time = self._compute_tree_properties(
            nums, adjacency_list, n
        )

        total_xor = subtree_xor[0]
        return self._find_minimum_score_optimized(
            subtree_xor, parent, in_time, out_time, total_xor, n
        )

    def _build_adjacency_list(self, edges: List[List[int]], n: int) -> List[List[int]]:
        """Build adjacency list representation of the tree."""
        adjacency_list = [[] for _ in range(n)]
        for node_a, node_b in edges:
            adjacency_list[node_a].append(node_b)
            adjacency_list[node_b].append(node_a)
        return adjacency_list

    def _compute_tree_properties(self, nums: List[int], adjacency_list: List[List[int]], n: int):
        """Compute subtree XOR, parent, and in/out times using iterative DFS."""
        subtree_xor = [0] * n
        parent = [0] * n
        in_time = [0] * n
        out_time = [0] * n
        time = 0

        # Iterative DFS using stack with (node, parent, is_post_order) tuples
        stack = [(0, -1, False)]

        while stack:
            node, parent_node, is_post_order = stack.pop()

            if not is_post_order:
                # Pre-order: set parent and in_time
                parent[node] = parent_node
                in_time[node] = time
                time += 1

                # Add post-order processing
                stack.append((node, parent_node, True))

                # Add children in reverse order for correct traversal
                for neighbor in reversed(adjacency_list[node]):
                    if neighbor != parent_node:
                        stack.append((neighbor, node, False))
            else:
                # Post-order: compute subtree XOR and out_time
                subtree_xor[node] = nums[node]
                for neighbor in adjacency_list[node]:
                    if neighbor != parent_node:
                        subtree_xor[node] ^= subtree_xor[neighbor]
                out_time[node] = time - 1

        return subtree_xor, parent, in_time, out_time

    def _find_minimum_score_optimized(self, subtree_xor: List[int], parent: List[int],
                                     in_time: List[int], out_time: List[int],
                                     total_xor: int, n: int) -> int:
        """Find minimum score by trying all valid node pairs as edge removals."""
        min_score = float('inf')

        for i in range(1, n):
            for j in range(i + 1, n):
                # Determine tree structure after removing edges to nodes i and j
                component_x, component_y, component_z = self._calculate_components(
                    i, j, subtree_xor, in_time, out_time, total_xor
                )

                # Calculate score difference
                max_component = max(component_x, component_y, component_z)
                min_component = min(component_x, component_y, component_z)
                current_score = max_component - min_component

                if current_score < min_score:
                    min_score = current_score

        return min_score

    def _calculate_components(self, i: int, j: int, subtree_xor: List[int],
                            in_time: List[int], out_time: List[int], total_xor: int):
        """Calculate XOR values of three components after removing edges to nodes i and j."""
        # Check ancestor-descendant relationship using in/out times
        if in_time[i] < in_time[j] <= out_time[i]:
            # j is descendant of i
            component_x = subtree_xor[j]
            component_y = subtree_xor[i] ^ subtree_xor[j]
            component_z = total_xor ^ subtree_xor[i]
        elif in_time[j] < in_time[i] <= out_time[j]:
            # i is descendant of j
            component_x = subtree_xor[i]
            component_y = subtree_xor[j] ^ subtree_xor[i]
            component_z = total_xor ^ subtree_xor[j]
        else:
            # i and j are in different subtrees
            component_x = subtree_xor[i]
            component_y = subtree_xor[j]
            component_z = total_xor ^ component_x ^ component_y

        return component_x, component_y, component_z
