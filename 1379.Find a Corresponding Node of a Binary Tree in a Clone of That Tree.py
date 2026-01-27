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
    def getTargetCopy(
        self, original: TreeNode, cloned: TreeNode, target: TreeNode
    ) -> TreeNode | None:
        """Find the corresponding node in a cloned binary tree.

        Intuition:
            Traverse both trees simultaneously. When we find the target in
            the original tree, the corresponding node in the cloned tree is
            at the same position.

        Approach:
            DFS both trees in parallel. When the current original node matches
            the target, return the current cloned node. Otherwise recurse into
            left and right subtrees.

        Complexity:
            Time: O(n)
            Space: O(h) where h is the tree height.
        """

        def dfs(
            original_node: TreeNode | None, cloned_node: TreeNode | None
        ) -> TreeNode | None:
            if original_node is None:
                return None
            if original_node is target:
                return cloned_node
            return dfs(original_node.left, cloned_node.left) or dfs(
                original_node.right, cloned_node.right
            )

        return dfs(original, cloned)
