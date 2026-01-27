class Solution:
    def preorderTraversal(self, root: TreeNode | None) -> list[int]:
        """Recursive DFS preorder traversal (root, left, right).

        Intuition:
            Preorder visits the root first, then recursively visits left and
            right subtrees. A simple recursive DFS collects values in order.

        Approach:
            1. Initialize a result list.
            2. Define a recursive helper that appends the node value, then
               recurses on left and right children.
            3. Return the collected result.

        Complexity:
            Time: O(n)
            Space: O(n) — result list plus O(h) recursion stack
        """

        def dfs(node: TreeNode | None) -> None:
            if node is None:
                return
            result.append(node.val)
            dfs(node.left)
            dfs(node.right)

        result = []
        dfs(root)
        return result
