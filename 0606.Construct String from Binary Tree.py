class Solution:
    def tree2str(self, root: "TreeNode | None") -> str:
        """Construct string from binary tree using preorder traversal with parentheses.

        Intuition:
            Represent the tree as a string where children are enclosed in
            parentheses. Empty left subtrees must be shown as () when a right
            child exists, but empty right subtrees can be omitted.

        Approach:
            1. Base case: return empty string for null nodes.
            2. Leaf node: return just the value.
            3. No right child: wrap only left subtree in parentheses.
            4. Both children: wrap both subtrees in separate parentheses.

        Complexity:
            Time: O(n)
            Space: O(n) for recursion stack
        """

        def dfs(node: "TreeNode | None") -> str:
            if node is None:
                return ""
            if node.left is None and node.right is None:
                return str(node.val)
            if node.right is None:
                return f"{node.val}({dfs(node.left)})"
            return f"{node.val}({dfs(node.left)})({dfs(node.right)})"

        return dfs(root)
