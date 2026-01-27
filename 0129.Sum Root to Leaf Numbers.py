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
    def sumNumbers(self, root: TreeNode | None) -> int:
        """DFS Path Accumulation Approach

        Intuition:
            Each root-to-leaf path represents a number formed by concatenating
            node values. We can accumulate the number as we traverse by multiplying
            the running sum by 10 and adding the current node value.

        Approach:
            Use DFS passing the accumulated sum. At each node, compute the new sum.
            At leaf nodes, return the accumulated value. For internal nodes, return
            the sum of left and right subtree results.

        Complexity:
            Time: O(n) where n is the number of nodes
            Space: O(h) where h is the height of the tree (recursion stack)
        """

        def dfs(node: TreeNode | None, accumulated: int) -> int:
            if node is None:
                return 0
            accumulated = accumulated * 10 + node.val
            if node.left is None and node.right is None:
                return accumulated
            return dfs(node.left, accumulated) + dfs(node.right, accumulated)

        return dfs(root, 0)
