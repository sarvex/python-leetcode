class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        """BST property-based traversal to find lowest common ancestor.

        Intuition:
            In a BST, the LCA is the first node whose value lies between p and q.
            If both targets are smaller, go left; if both are larger, go right.

        Approach:
            Traverse from root. If current value is less than both targets, move
            right. If greater than both, move left. Otherwise, the current node
            is the lowest common ancestor.

        Complexity:
            Time: O(h) where h is the height of the tree
            Space: O(1)
        """
        while True:
            if root.val < min(p.val, q.val):
                root = root.right
            elif root.val > max(p.val, q.val):
                root = root.left
            else:
                return root
