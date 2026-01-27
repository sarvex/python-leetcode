# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        """In-order DFS relinking nodes into a right-skewed tree.

        Intuition:
            An in-order traversal of a BST visits nodes in sorted order.
            Relink each visited node as the right child of the previous node.

        Approach:
            1. Create a dummy node as the starting point.
            2. Perform in-order DFS, setting each visited node as the right
               child of the previous node and clearing its left child.
            3. Return dummy.right as the new root.

        Complexity:
            Time: O(n)
            Space: O(h) where h is the tree height (recursion stack).
        """

        def dfs(node: TreeNode | None) -> None:
            if node is None:
                return
            nonlocal previous
            dfs(node.left)
            previous.right = node
            node.left = None
            previous = node
            dfs(node.right)

        dummy = previous = TreeNode(right=root)
        dfs(root)
        return dummy.right
