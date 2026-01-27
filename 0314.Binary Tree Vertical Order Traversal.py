from collections import defaultdict


class Solution:
    def verticalOrder(self, root: "TreeNode | None") -> list[list[int]]:
        """DFS with column offset tracking and depth-based sorting.

        Intuition:
            Assign each node a column offset. Nodes in the same column should
            appear sorted by their depth (top to bottom).

        Approach:
            1. DFS the tree, recording (depth, value) for each column offset.
            2. Sort columns by offset, then sort nodes within each column by depth.
            3. Extract values from sorted nodes.

        Complexity:
            Time: O(n log n) where n is the number of nodes
            Space: O(n) for the column map
        """

        def dfs(node: "TreeNode | None", depth: int, offset: int) -> None:
            if node is None:
                return
            columns[offset].append((depth, node.val))
            dfs(node.left, depth + 1, offset - 1)
            dfs(node.right, depth + 1, offset + 1)

        columns: dict[int, list[tuple[int, int]]] = defaultdict(list)
        dfs(root, 0, 0)
        result = []
        for _, nodes in sorted(columns.items()):
            nodes.sort(key=lambda x: x[0])
            result.append([x[1] for x in nodes])
        return result
