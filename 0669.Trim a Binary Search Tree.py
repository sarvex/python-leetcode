class Solution:
    def trimBST(
        self, root: "TreeNode | None", low: int, high: int
    ) -> "TreeNode | None":
        """Recursive BST trimming to keep only values within [low, high].

        Intuition:
        Use BST property: if a node's value is too high, only its left subtree
        may contain valid values; if too low, only the right subtree.

        Approach:
        1. If node is None, return None.
        2. If node value > high, trim and return result from left subtree.
        3. If node value < low, trim and return result from right subtree.
        4. Otherwise, recursively trim both subtrees and keep the node.

        Complexity:
        Time: O(n)
        Space: O(n) for recursion stack
        """

        def dfs(node: "TreeNode | None") -> "TreeNode | None":
            if node is None:
                return node
            if node.val > high:
                return dfs(node.left)
            if node.val < low:
                return dfs(node.right)
            node.left = dfs(node.left)
            node.right = dfs(node.right)
            return node

        return dfs(root)
