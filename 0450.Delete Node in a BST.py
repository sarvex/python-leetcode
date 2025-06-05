from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        """Successor-based BST deletion with recursive approach

        Intuition: When deleting a node from a BST, we need to maintain the BST property.
        For leaf nodes, we can simply delete them. For nodes with one child, we replace
        the node with its child. For nodes with two children, we find the successor
        (smallest node in right subtree) and use it to replace the deleted node.

        Approach:
        1. Recursively search for the node to delete
        2. If node is found, handle three cases:
           - No children: Return None
           - One child: Return the existing child
           - Two children: Find successor, connect left subtree to successor, return right subtree

        Complexity:
        Time: O(h) where h is the height of the tree (O(log n) for balanced trees, O(n) worst case)
        Space: O(h) for recursion stack
        """
        if not root:
            return None

        # Search for the node to delete
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:  # Found the node to delete
            # Case 1 & 2: No left child or no children
            if not root.left:
                return root.right
            # Case 2: No right child
            if not root.right:
                return root.left

            # Case 3: Two children - find successor (min value in right subtree)
            def find_min(node: TreeNode) -> TreeNode:
                while node.left:
                    node = node.left
                return node

            # Get successor and connect left subtree to it
            successor = find_min(root.right)
            successor.left = root.left

            # Return right subtree as new root of this subtree
            return root.right

        return root
