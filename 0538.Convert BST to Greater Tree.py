class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        """Reverse inorder traversal to convert BST to Greater Tree.

        Intuition:
            In a BST, visiting nodes in reverse inorder (right-root-left)
            processes values from largest to smallest. We can accumulate
            a running sum to transform each node.

        Approach:
            Perform reverse inorder DFS, maintaining a running sum of all
            visited values. Update each node's value to include the sum of
            all greater values.

        Complexity:
            Time: O(n)
            Space: O(h) where h is tree height
        """

        def dfs(node: TreeNode | None) -> None:
            nonlocal running_sum
            if node is None:
                return
            dfs(node.right)
            running_sum += node.val
            node.val = running_sum
            dfs(node.left)

        running_sum = 0
        dfs(root)
        return root
