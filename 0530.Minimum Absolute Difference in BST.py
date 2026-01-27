from math import inf


class Solution:
    def getMinimumDifference(self, root: TreeNode | None) -> int:
        """Inorder traversal to find minimum difference between BST nodes.

        Intuition:
            Inorder traversal of a BST produces sorted values. The minimum
            difference must be between consecutive values in this order.

        Approach:
            Perform inorder DFS, tracking the previous value. At each node,
            compute the difference with the previous value and update the
            minimum.

        Complexity:
            Time: O(n)
            Space: O(h) where h is tree height
        """

        def dfs(node: TreeNode | None) -> None:
            if node is None:
                return
            dfs(node.left)
            nonlocal previous, min_diff
            min_diff = min(min_diff, node.val - previous)
            previous = node.val
            dfs(node.right)

        previous = -inf
        min_diff = inf
        dfs(root)
        return min_diff
