class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        Post-order traversal to find lowest common ancestor

        Intuition:
        If we find either p or q, that node could be the LCA if the other node is in its subtree.
        If p and q are in different subtrees, their parent is the LCA.

        Approach:
        1. Use post-order traversal (left, right, root) to search for nodes p and q
        2. If current node is p or q or None, return it
        3. Recursively search left and right subtrees
        4. If both left and right return non-None values, current node is LCA
        5. Otherwise, return whichever subtree found a target node

        Complexity:
        Time: O(n) where n is the number of nodes in the tree
        Space: O(h) where h is the height of the tree (recursion stack)
        """
        # Base case: if root is None or one of the target nodes
        if root in (None, p, q):
            return root

        # Search in left and right subtrees
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        # If both subtrees found something, this is the LCA
        # Otherwise return the non-None result
        return root if left and right else (left or right)
