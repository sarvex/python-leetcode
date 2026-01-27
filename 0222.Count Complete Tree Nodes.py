class Solution:
    def countNodes(self, root: TreeNode | None) -> int:
        """Recursive counting of all nodes in a complete binary tree.

        Intuition:
            A simple recursive traversal counts every node. For a complete tree,
            optimized approaches exist, but recursion is clean and correct.

        Approach:
            1. If the root is None, return 0.
            2. Recursively count left and right subtree nodes.
            3. Return 1 + left_count + right_count.

        Complexity:
            Time: O(n)
            Space: O(log n) for the recursion stack
        """
        if root is None:
            return 0
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
