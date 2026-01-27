from math import inf


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
    def maxPathSum(self, root: TreeNode | None) -> int:
        """DFS Post-Order Traversal Approach

        Intuition:
            The maximum path sum can pass through any node as the highest point.
            At each node, we consider the best path through it (left + node + right)
            while returning the best single-branch path to the parent.

        Approach:
            Use DFS to compute the maximum gain from each subtree. At each node,
            calculate left and right gains (clamped to 0 to ignore negative paths).
            Update the global answer with the path through the current node, then
            return the best single-branch gain.

        Complexity:
            Time: O(n) where n is the number of nodes
            Space: O(h) where h is the height of the tree (recursion stack)
        """

        def dfs(node: TreeNode | None) -> int:
            if node is None:
                return 0
            left_gain = max(0, dfs(node.left))
            right_gain = max(0, dfs(node.right))
            nonlocal result
            result = max(result, node.val + left_gain + right_gain)
            return node.val + max(left_gain, right_gain)

        result = -inf
        dfs(root)
        return result
