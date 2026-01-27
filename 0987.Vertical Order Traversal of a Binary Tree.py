class TreeNode:
    def __init__(
        self,
        val: int = 0,
        left: "TreeNode | None" = None,
        right: "TreeNode | None" = None,
    ):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def verticalTraversal(self, root: TreeNode | None) -> list[list[int]]:
        """Return vertical order traversal of a binary tree.

        Intuition:
            Assign column and row indices to each node via DFS, then sort by
            column, row, and value to produce the correct ordering.

        Approach:
            DFS to collect (column, row, value) tuples. Sort the tuples, then
            group consecutive nodes with the same column index into sublists.

        Complexity:
            Time: O(n log n) for sorting all nodes
            Space: O(n) to store all node tuples
        """

        def dfs(node: TreeNode | None, row: int, col: int) -> None:
            if node is None:
                return
            nodes.append((col, row, node.val))
            dfs(node.left, row + 1, col - 1)
            dfs(node.right, row + 1, col + 1)

        nodes: list[tuple[int, int, int]] = []
        dfs(root, 0, 0)
        nodes.sort()
        result: list[list[int]] = []
        prev_col = -2000
        for col, _, val in nodes:
            if prev_col != col:
                result.append([])
                prev_col = col
            result[-1].append(val)
        return result
