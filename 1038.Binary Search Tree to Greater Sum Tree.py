# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        """Binary Search Tree to Greater Sum Tree via reverse inorder traversal.

        Intuition:
            In a BST, reverse inorder traversal (right -> node -> left) visits
            nodes in descending order. Accumulate a running sum to compute the
            greater sum for each node.

        Approach:
            Traverse the tree in reverse inorder. Maintain a running sum of all
            visited node values. Update each node's value to include the sum of
            all greater nodes.

        Complexity:
            Time: O(n)
            Space: O(h) where h is tree height
        """

        def dfs(node: TreeNode | None) -> None:
            nonlocal running_sum
            if node is None:
                return
            dfs(node.right)
            running_sum += node.val
            node.val = running_sum
            dfs(node.left)

        running_sum = 0
        dfs(root)
        return root
