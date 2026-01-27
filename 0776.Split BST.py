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
    def splitBST(self, root: TreeNode | None, target: int) -> list[TreeNode | None]:
        """Recursively split BST into two trees around a target value.

        Intuition:
            At each node, decide whether it belongs to the left tree (<= target)
            or right tree (> target). Recursively split the appropriate subtree
            and reconnect the pointers.

        Approach:
            1. If root is None, return [None, None]
            2. If root.val <= target, the root belongs to the left tree; recurse
               on the right subtree and attach the left part as root.right
            3. If root.val > target, the root belongs to the right tree; recurse
               on the left subtree and attach the right part as root.left

        Complexity:
            Time: O(h) where h is the tree height
            Space: O(h) for recursion stack
        """

        def dfs(node: TreeNode | None) -> list[TreeNode | None]:
            if node is None:
                return [None, None]
            if node.val <= target:
                left_part, right_part = dfs(node.right)
                node.right = left_part
                return [node, right_part]
            else:
                left_part, right_part = dfs(node.left)
                node.left = right_part
                return [left_part, node]

        return dfs(root)
