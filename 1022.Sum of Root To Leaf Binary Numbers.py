# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        """Sum of Root To Leaf Binary Numbers via DFS.

        Intuition:
            Each root-to-leaf path represents a binary number. Accumulate the
            binary value as we traverse, shifting left and OR-ing the current
            node value.

        Approach:
            Use recursive DFS passing the accumulated binary value. At each
            node, update the value as (current << 1) | node.val. At leaf nodes,
            return the accumulated value. Sum results from left and right subtrees.

        Complexity:
            Time: O(n)
            Space: O(h) where h is tree height
        """

        def dfs(node: TreeNode | None, accumulated: int) -> int:
            if node is None:
                return 0
            accumulated = (accumulated << 1) | node.val
            if node.left is None and node.right is None:
                return accumulated
            return dfs(node.left, accumulated) + dfs(node.right, accumulated)

        return dfs(root, 0)
