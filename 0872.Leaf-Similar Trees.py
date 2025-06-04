from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        """Determine if two binary trees are leaf-similar.

        Approach: DFS with leaf sequence collection

        Intuition: Two trees are leaf-similar if their leaf value sequences are the same.
        We can perform DFS on both trees to collect their leaf values and then compare.

        Approach: Use DFS to traverse each tree and collect leaf node values in a list.
        A leaf node is one with no children. Compare the two resulting lists for equality.

        Complexity:
            Time: O(n + m), where n and m are the number of nodes in the two trees
            Space: O(h1 + h2 + l), where h1 and h2 are the heights of the trees and l is the number of leaf nodes
        """
        def dfs(root: Optional[TreeNode]) -> List[int]:
            """Collect leaf values using DFS."""
            if not root:
                return []
            if not root.left and not root.right:
                return [root.val]
            return dfs(root.left) + dfs(root.right)

        return dfs(root1) == dfs(root2)
