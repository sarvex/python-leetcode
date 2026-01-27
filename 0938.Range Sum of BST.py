# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode | None, low: int, high: int) -> int:
        """DFS with BST pruning to sum values within range.

        Intuition:
            Leverage BST property to skip entire subtrees when the current
            node value is outside the target range.

        Approach:
            1. If node is None, return 0.
            2. Include current value if within [low, high].
            3. Recurse left only if current value > low (left subtree may have valid nodes).
            4. Recurse right only if current value < high (right subtree may have valid nodes).

        Complexity:
            Time: O(n) — visits each node at most once
            Space: O(h) — recursion stack depth equals tree height
        """

        def dfs(node: TreeNode | None) -> int:
            if node is None:
                return 0
            value = node.val
            total = value if low <= value <= high else 0
            if value > low:
                total += dfs(node.left)
            if value < high:
                total += dfs(node.right)
            return total

        return dfs(root)
