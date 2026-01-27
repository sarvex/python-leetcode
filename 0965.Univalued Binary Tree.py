# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        """DFS checking all nodes share the same value as root.

        Intuition:
            A univalued tree has every node with the same value. Simply compare
            each node's value against the root's value during traversal.

        Approach:
            1. Recursively traverse the tree.
            2. For each node, check if its value equals the root's value.
            3. Return True only if all nodes match.

        Complexity:
            Time: O(n) — visit every node once
            Space: O(h) — recursion stack depth equals tree height
        """

        def dfs(node: TreeNode | None) -> bool:
            if node is None:
                return True
            return node.val == root.val and dfs(node.left) and dfs(node.right)

        return dfs(root)
