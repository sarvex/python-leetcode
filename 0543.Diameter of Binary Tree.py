class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        """DFS computing depth while tracking maximum diameter.

        Intuition:
            The diameter through any node is the sum of left and right subtree
            depths. The overall diameter is the maximum across all nodes.

        Approach:
            Use post-order DFS returning the depth of each subtree. At each
            node, update the global maximum with left_depth + right_depth.

        Complexity:
            Time: O(n)
            Space: O(h) where h is tree height
        """

        def dfs(node: TreeNode | None) -> int:
            if node is None:
                return 0
            nonlocal max_diameter
            left_depth, right_depth = dfs(node.left), dfs(node.right)
            max_diameter = max(max_diameter, left_depth + right_depth)
            return 1 + max(left_depth, right_depth)

        max_diameter = 0
        dfs(root)
        return max_diameter
