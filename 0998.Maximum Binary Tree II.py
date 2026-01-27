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
    def insertIntoMaxTree(self, root: TreeNode | None, val: int) -> TreeNode | None:
        """Insert a value into the maximum binary tree as if appended to the array.

        Intuition:
            The new value is appended at the end, so it can only appear on the
            rightmost path. If it is larger than the current node, it becomes the
            new root with the old tree as its left child.

        Approach:
            Recursively walk the right spine. If the current node is None or its
            value is less than val, create a new node with the current subtree as
            the left child. Otherwise recurse into the right subtree.

        Complexity:
            Time: O(h) where h is the height of the tree
            Space: O(h) for recursion stack
        """
        if root is None or root.val < val:
            return TreeNode(val, root)
        root.right = self.insertIntoMaxTree(root.right, val)
        return root
