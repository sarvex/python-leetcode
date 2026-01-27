class Solution:
    def removeLeafNodes(self, root: TreeNode | None, target: int) -> TreeNode | None:
        """Remove all leaf nodes with the given target value repeatedly.

        Intuition:
            Post-order traversal naturally handles cascading deletions: after
            removing children, a parent may become a new leaf to remove.

        Approach:
            Recursively process left and right subtrees first, then check if
            the current node is a leaf with the target value.

        Complexity:
            Time: O(n)
            Space: O(h) where h is the tree height
        """
        if root is None:
            return None
        root.left = self.removeLeafNodes(root.left, target)
        root.right = self.removeLeafNodes(root.right, target)
        if root.left is None and root.right is None and root.val == target:
            return None
        return root
