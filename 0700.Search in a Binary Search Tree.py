from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        """Binary search tree property-based recursive search.

        Intuition:
        BST has a key property: for any node, all values in left subtree are smaller,
        and all values in right subtree are greater. We can leverage this to efficiently
        search by comparing the target value with current node value and deciding which
        subtree to search next.

        Approach:
        1. If root is None or root's value equals target value, return root
        2. If target value is less than root's value, search in left subtree
        3. If target value is greater than root's value, search in right subtree
        4. Use recursion to implement the search

        Complexity:
        Time: O(h) where h is the height of the tree (O(log n) for balanced BST, O(n) worst case)
        Space: O(h) for recursion stack
        """
        if root is None or root.val == val:
            return root

        if val < root.val:
            return self.searchBST(root.left, val)
        return self.searchBST(root.right, val)
