class Solution:
    def pruneTree(self, root: TreeNode | None) -> TreeNode | None:
        """Recursively prune subtrees that contain no 1s.

        Intuition:
            Post-order traversal: prune children first, then check if the
            current node has value 0 with no children — if so, prune it.

        Approach:
            1. Recursively prune left and right subtrees.
            2. If the current node's value is 0 and both children are None,
               return None to remove it.
            3. Otherwise, return the node.

        Complexity:
            Time: O(n)
            Space: O(h) where h = tree height
        """
        if root is None:
            return None
        root.left = self.pruneTree(root.left)
        root.right = self.pruneTree(root.right)
        if root.val == 0 and root.left is None and root.right is None:
            return None
        return root
