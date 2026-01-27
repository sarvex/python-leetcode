class Solution:
    def sumOfLeftLeaves(self, root: "TreeNode | None") -> int:
        """Recursive traversal summing left leaf values.

        Intuition:
            A left leaf is a node that is the left child of its parent
            and has no children. We can check this condition during
            recursive traversal.

        Approach:
            1. If root is None, return 0.
            2. Recursively sum left leaves in the right subtree.
            3. For the left child, check if it is a leaf (both children None).
            4. If it is a leaf, add its value; otherwise recurse into it.

        Complexity:
            Time: O(n) where n is the number of nodes
            Space: O(h) where h is the height of the tree
        """
        if root is None:
            return 0
        total = self.sumOfLeftLeaves(root.right)
        if root.left:
            if root.left.left == root.left.right:
                total += root.left.val
            else:
                total += self.sumOfLeftLeaves(root.left)
        return total
