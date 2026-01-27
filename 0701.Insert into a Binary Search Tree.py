class Solution:
    def insertIntoBST(self, root: TreeNode | None, val: int) -> TreeNode | None:
        """Recursive BST insertion following left/right comparison.

        Intuition:
            In a BST, values less than the current node go left and greater
            values go right. Recurse until finding a None spot to insert.

        Approach:
            1. If the current node is None, create a new node with the value.
            2. If val < current node value, recurse into left subtree.
            3. Otherwise, recurse into right subtree.
            4. Return the root to maintain tree structure.

        Complexity:
            Time: O(h) where h is the tree height
            Space: O(h) for the recursion stack
        """
        if root is None:
            return TreeNode(val)
        if root.val > val:
            root.left = self.insertIntoBST(root.left, val)
        else:
            root.right = self.insertIntoBST(root.right, val)
        return root
