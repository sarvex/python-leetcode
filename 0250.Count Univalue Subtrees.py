class Solution:
    def countUnivalSubtrees(self, root: "TreeNode | None") -> int:
        """Post-order DFS counting subtrees where all nodes share the same value.

        Intuition:
            A subtree is uni-value if both children are uni-value subtrees and
            their values match the root. Process bottom-up with post-order DFS.

        Approach:
            Recursively check left and right subtrees. A node forms a uni-value
            subtree if both children are uni-value (or null) and their values
            equal the current node's value. Count each valid subtree.

        Complexity:
            Time: O(n) where n is the number of nodes
            Space: O(h) where h is the tree height for recursion stack
        """

        def dfs(node: "TreeNode | None") -> bool:
            if node is None:
                return True
            left_uniform, right_uniform = dfs(node.left), dfs(node.right)
            if not left_uniform or not right_uniform:
                return False
            left_val = node.val if node.left is None else node.left.val
            right_val = node.val if node.right is None else node.right.val
            if left_val == right_val == node.val:
                nonlocal count
                count += 1
                return True
            return False

        count = 0
        dfs(root)
        return count
