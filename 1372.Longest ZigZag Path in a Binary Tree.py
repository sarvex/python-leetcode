from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        """DFS with path direction tracking

        Intuition:
        A zigzag path alternates between left and right child nodes. We need to track
        the current direction and length of zigzag paths starting from each node.

        Approach:
        Use DFS to traverse the tree. For each node, track two values:
        1. Length of zigzag path if we came from parent to this node as a left child
        2. Length of zigzag path if we came from parent to this node as a right child
        Update the global maximum length during traversal.

        Complexity:
        Time: O(n) where n is the number of nodes in the tree
        Space: O(h) where h is the height of the tree (recursion stack)
        """
        def dfs(node: Optional[TreeNode], left: int, right: int) -> None:
            if node is None:
                return

            nonlocal length
            length = max(length, left, right)

            # If we go left, we can only continue a zigzag if we came from right
            dfs(node.left, right + 1, 0)

            # If we go right, we can only continue a zigzag if we came from left
            dfs(node.right, 0, left + 1)

        length = 0
        dfs(root, 0, 0)
        return length
