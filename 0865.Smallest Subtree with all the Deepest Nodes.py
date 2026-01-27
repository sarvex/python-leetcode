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
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        """Post-order DFS comparing subtree depths to find the LCA of deepest nodes.

        Intuition:
        The smallest subtree containing all deepest nodes is the lowest common
        ancestor of all deepest leaves. By tracking depth from each subtree,
        we can identify where left and right depths match.

        Approach:
        1. DFS returns (subtree_root, depth) for each node
        2. If left depth > right depth, the answer is in the left subtree
        3. If right depth > left depth, the answer is in the right subtree
        4. If depths are equal, current node is the LCA of deepest nodes

        Complexity:
        Time: O(n) where n is the number of nodes
        Space: O(h) where h is the tree height for recursion stack
        """

        def dfs(node: TreeNode | None) -> tuple[TreeNode | None, int]:
            if node is None:
                return None, 0
            left_result, left_depth = dfs(node.left)
            right_result, right_depth = dfs(node.right)
            if left_depth > right_depth:
                return left_result, left_depth + 1
            if left_depth < right_depth:
                return right_result, right_depth + 1
            return node, left_depth + 1

        return dfs(root)[0]
