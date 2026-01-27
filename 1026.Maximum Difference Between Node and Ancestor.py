# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: TreeNode | None) -> int:
        """Maximum Difference Between Node and Ancestor via DFS min/max tracking.

        Intuition:
            The maximum difference between an ancestor and a descendant equals
            the difference between the maximum and minimum values along any
            root-to-leaf path.

        Approach:
            DFS while propagating the current path's min and max values. At
            each node, compute the difference with both the running min and
            max, then update them and recurse into children.

        Complexity:
            Time: O(n)
            Space: O(h) where h is tree height
        """

        def dfs(node: TreeNode | None, min_val: int, max_val: int) -> None:
            if node is None:
                return
            nonlocal result
            result = max(result, abs(min_val - node.val), abs(max_val - node.val))
            min_val = min(min_val, node.val)
            max_val = max(max_val, node.val)
            dfs(node.left, min_val, max_val)
            dfs(node.right, min_val, max_val)

        result = 0
        dfs(root, root.val, root.val)
        return result
