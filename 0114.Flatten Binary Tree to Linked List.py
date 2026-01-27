class Solution:
    def flatten(self, root: TreeNode | None) -> None:
        """Iterative Morris-Style Flattening

        Intuition:
            To flatten in-place to a right-skewed linked list in preorder,
            for each node with a left child, find the rightmost node of the
            left subtree and link it to the current node's right child. Then
            move the left subtree to the right.

        Approach:
            Iterate through the tree. For each node with a left child, find
            the predecessor (rightmost node of the left subtree). Set the
            predecessor's right to the current node's right child. Move the
            left subtree to the right and set left to None. Advance to the
            next right node.

        Complexity:
            Time: O(n)
            Space: O(1)
        """
        while root:
            if root.left:
                predecessor = root.left
                while predecessor.right:
                    predecessor = predecessor.right
                predecessor.right = root.right
                root.right = root.left
                root.left = None
            root = root.right
