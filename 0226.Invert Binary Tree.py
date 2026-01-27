class Solution:
    def invertTree(self, root: TreeNode | None) -> TreeNode | None:
        """Recursive DFS to swap left and right children at every node.

        Intuition:
            Inverting a binary tree means swapping left and right subtrees
            at every node, which naturally fits a recursive approach.

        Approach:
            1. If the node is None, return.
            2. Swap its left and right children.
            3. Recursively invert both subtrees.

        Complexity:
            Time: O(n)
            Space: O(h) where h is the tree height (recursion stack)
        """

        def dfs(node: TreeNode | None) -> None:
            if node is None:
                return
            node.left, node.right = node.right, node.left
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return root
