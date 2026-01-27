from math import inf


class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:
        """Inorder Traversal Validation

        Intuition:
            A valid BST has an inorder traversal that produces strictly
            increasing values. We can validate by tracking the previously
            visited value during inorder traversal.

        Approach:
            Perform an inorder DFS traversal. Maintain a nonlocal variable
            tracking the previous node's value. At each node, verify that the
            current value is strictly greater than the previous value. Return
            False immediately if the invariant is violated.

        Complexity:
            Time: O(n)
            Space: O(n) for recursion stack
        """

        def dfs(node: TreeNode | None) -> bool:
            if node is None:
                return True
            if not dfs(node.left):
                return False
            nonlocal prev
            if prev >= node.val:
                return False
            prev = node.val
            return dfs(node.right)

        prev = -inf
        return dfs(root)
