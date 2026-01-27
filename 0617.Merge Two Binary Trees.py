class Solution:
    def mergeTrees(
        self, root1: "TreeNode | None", root2: "TreeNode | None"
    ) -> "TreeNode | None":
        """Merge two binary trees by summing overlapping node values recursively.

        Intuition:
            At each position, if both trees have a node, sum their values.
            If only one tree has a node, use that node directly.

        Approach:
            1. If either root is None, return the other root.
            2. Create a new node with the sum of both values.
            3. Recursively merge left and right subtrees.

        Complexity:
            Time: O(min(m, n)) where m and n are tree sizes
            Space: O(min(m, n)) for recursion stack
        """
        if root1 is None:
            return root2
        if root2 is None:
            return root1
        node = TreeNode(root1.val + root2.val)
        node.left = self.mergeTrees(root1.left, root2.left)
        node.right = self.mergeTrees(root1.right, root2.right)
        return node
