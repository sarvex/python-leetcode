import math


class TreeNode:
    def __init__(
        self,
        val: int = 0,
        left: "TreeNode | None" = None,
        right: "TreeNode | None" = None,
    ) -> None:
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDiffInBST(self, root: TreeNode | None) -> int:
        """In-order traversal tracking previous node to find minimum difference.

        Intuition:
            An in-order traversal of a BST visits nodes in ascending order. The
            minimum difference must occur between two consecutive nodes in this
            sorted sequence.

        Approach:
            1. Perform in-order DFS traversal
            2. Track the previous node's value
            3. At each node, compute the difference with the previous value
            4. Update the minimum difference

        Complexity:
            Time: O(n) where n is the number of nodes
            Space: O(h) where h is the tree height for recursion stack
        """

        def dfs(node: TreeNode | None) -> None:
            if node is None:
                return
            dfs(node.left)
            nonlocal previous, min_diff
            min_diff = min(min_diff, node.val - previous)
            previous = node.val
            dfs(node.right)

        previous = -math.inf
        min_diff = math.inf
        dfs(root)
        return int(min_diff)
