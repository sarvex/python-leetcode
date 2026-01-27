class TreeNode:
    def __init__(
        self,
        val: int = 0,
        left: "TreeNode | None" = None,
        right: "TreeNode | None" = None,
    ) -> None:
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: TreeNode | None) -> list[int]:
        """Recursive Inorder Traversal

        Intuition:
            Inorder traversal visits left subtree, then root, then right
            subtree. A recursive approach directly mirrors this definition.

        Approach:
            Define a nested DFS function that recurses on the left child,
            appends the current node's value, then recurses on the right child.

        Complexity:
            Time: O(n)
            Space: O(n) for recursion stack and result list
        """

        def dfs(node: TreeNode | None) -> None:
            if node is None:
                return
            dfs(node.left)
            result.append(node.val)
            dfs(node.right)

        result: list[int] = []
        dfs(root)
        return result
