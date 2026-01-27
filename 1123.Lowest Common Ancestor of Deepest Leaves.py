# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: TreeNode | None) -> TreeNode | None:
        """Find the lowest common ancestor of the deepest leaves.

        Intuition:
            The LCA of the deepest leaves is the deepest node whose left and
            right subtrees have equal maximum depth.

        Approach:
            Use DFS returning (ancestor, depth) pairs. If left depth exceeds
            right, propagate the left ancestor; if right exceeds left,
            propagate right. When depths are equal, the current node is the LCA.

        Complexity:
            Time: O(n) where n is the number of nodes
            Space: O(h) where h is the height of the tree
        """

        def dfs(node: TreeNode | None) -> tuple[TreeNode | None, int]:
            if node is None:
                return None, 0
            left_ancestor, left_depth = dfs(node.left)
            right_ancestor, right_depth = dfs(node.right)
            if left_depth > right_depth:
                return left_ancestor, left_depth + 1
            if left_depth < right_depth:
                return right_ancestor, right_depth + 1
            return node, left_depth + 1

        return dfs(root)[0]
