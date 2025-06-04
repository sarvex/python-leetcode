from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """Recursive DFS approach to find maximum depth of binary tree

        Intuition:
        The depth of a tree is the length of the longest path from root to leaf.
        If we know the depth of left and right subtrees, the overall depth is
        1 (for the root) plus the maximum of those depths.

        Approach:
        Use recursive DFS to calculate the depth of each subtree:
        1. Base case: If node is None, depth is 0
        2. Recursively find depth of left and right subtrees
        3. Return 1 (current node) + max(left depth, right depth)

        Complexity:
        Time: O(n) where n is the number of nodes (visit each node once)
        Space: O(h) where h is the height of tree (recursion stack space)
        """
        if not root:
            return 0

        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)

        return 1 + max(left_depth, right_depth)
