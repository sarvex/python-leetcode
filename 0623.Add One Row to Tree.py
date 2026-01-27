class Solution:
    def addOneRow(
        self, root: "TreeNode | None", val: int, depth: int
    ) -> "TreeNode | None":
        """Add a row of nodes with given value at specified depth using DFS.

        Intuition:
            Traverse the tree to depth-1 level, then insert new nodes between
            each node and its children at that level.

        Approach:
            1. Special case: if depth is 1, create a new root with the old root as left child.
            2. DFS to level depth-1, then replace each node's children with new
               nodes that have the original children as their subtrees.

        Complexity:
            Time: O(n)
            Space: O(n) for recursion stack
        """

        def dfs(node: "TreeNode | None", current_depth: int) -> None:
            if node is None:
                return
            if current_depth == depth - 1:
                node.left = TreeNode(val, node.left, None)
                node.right = TreeNode(val, None, node.right)
                return
            dfs(node.left, current_depth + 1)
            dfs(node.right, current_depth + 1)

        if depth == 1:
            return TreeNode(val, root)
        dfs(root, 1)
        return root
