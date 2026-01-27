class Solution:
    def inorderSuccessor(self, root: "TreeNode", p: "TreeNode") -> "TreeNode | None":
        """BST property-based search for inorder successor.

        Intuition:
            The inorder successor of a node in a BST is the smallest node
            with a value greater than p's value. We can leverage BST ordering
            to find it without a full inorder traversal.

        Approach:
            1. Traverse the tree starting from root.
            2. If root's value is greater than p's, it could be the successor;
               record it and move left to find a closer candidate.
            3. Otherwise, move right since the successor must be larger.

        Complexity:
            Time: O(h) where h is the height of the tree
            Space: O(1)
        """
        successor = None
        while root:
            if root.val > p.val:
                successor = root
                root = root.left
            else:
                root = root.right
        return successor
