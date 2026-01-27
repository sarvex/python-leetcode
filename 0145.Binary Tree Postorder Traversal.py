class Solution:
    def postorderTraversal(self, root: TreeNode | None) -> list[int]:
        """Recursive DFS postorder traversal (left, right, root).

        Intuition:
            Postorder visits left subtree, right subtree, then the root.
            A recursive DFS naturally captures this ordering.

        Approach:
            1. Initialize a result list.
            2. Define a recursive helper that recurses on left, then right,
               then appends the current node value.
            3. Return the collected result.

        Complexity:
            Time: O(n)
            Space: O(n) — result list plus O(h) recursion stack
        """

        def dfs(node: TreeNode | None) -> None:
            if node is None:
                return
            dfs(node.left)
            dfs(node.right)
            result.append(node.val)

        result = []
        dfs(root)
        return result
