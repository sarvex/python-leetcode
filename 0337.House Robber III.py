class Solution:
    def rob(self, root: "TreeNode | None") -> int:
        """Tree DP returning (rob_current, skip_current) for each node.

        Intuition:
            At each node we have two choices: rob it (and skip children) or
            skip it (and take the best of robbing or skipping each child).

        Approach:
            1. Post-order DFS returns a pair (rob_this, skip_this) for each node.
            2. rob_this = node.val + skip_left + skip_right
            3. skip_this = max(rob_left, skip_left) + max(rob_right, skip_right)
            4. Answer is max of the two values at the root.

        Complexity:
            Time: O(n) where n is the number of nodes
            Space: O(h) where h is the height of the tree
        """

        def dfs(node: "TreeNode | None") -> tuple[int, int]:
            if node is None:
                return 0, 0
            rob_left, skip_left = dfs(node.left)
            rob_right, skip_right = dfs(node.right)
            return node.val + skip_left + skip_right, max(rob_left, skip_left) + max(
                rob_right, skip_right
            )

        return max(dfs(root))
