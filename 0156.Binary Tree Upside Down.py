class Solution:
    def upsideDownBinaryTree(self, root: TreeNode | None) -> TreeNode | None:
        """Recursive Tree Transformation.

        Intuition:
            The leftmost node becomes the new root. Each left child's right
            pointer becomes its parent, and its left pointer becomes the
            parent's right child.

        Approach:
            Recursively process the left subtree to find the new root. Then
            rewire: the current left child's right points to current node,
            left child's left points to current node's right child. Clear
            the current node's children.

        Complexity:
            Time: O(n) visiting each node once
            Space: O(n) recursion stack in worst case (skewed tree)
        """
        if root is None or root.left is None:
            return root
        new_root = self.upsideDownBinaryTree(root.left)
        root.left.right = root
        root.left.left = root.right
        root.left = None
        root.right = None
        return new_root
