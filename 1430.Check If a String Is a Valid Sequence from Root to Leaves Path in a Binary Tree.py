# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isValidSequence(self, root: TreeNode, arr: list[int]) -> bool:
        """Check if array matches a root-to-leaf path in binary tree.

        Intuition:
            DFS traversal comparing each node value with the corresponding
            array element at that depth.

        Approach:
            Recursively traverse the tree tracking the current index in the
            array. At each node, verify the value matches. At a leaf, check
            that the entire array has been consumed.

        Complexity:
            Time: O(n) where n is the number of nodes
            Space: O(h) where h is the tree height for recursion stack
        """

        def dfs(node: TreeNode | None, index: int) -> bool:
            if node is None or node.val != arr[index]:
                return False
            if index == len(arr) - 1:
                return node.left is None and node.right is None
            return dfs(node.left, index + 1) or dfs(node.right, index + 1)

        return dfs(root, 0)
