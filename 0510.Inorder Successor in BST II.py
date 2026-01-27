class Solution:
    def inorderSuccessor(self, node: "Node") -> "Node | None":
        """Find inorder successor using parent pointers.

        Intuition:
            If the node has a right child, the successor is the leftmost node
            in the right subtree. Otherwise, traverse up to find the first
            ancestor where the node is in the left subtree.

        Approach:
            Case 1: Go right then all the way left.
            Case 2: Go up while the current node is the right child of its parent.
            The parent at that point is the successor.

        Complexity:
            Time: O(h) where h is tree height
            Space: O(1)
        """
        if node.right:
            node = node.right
            while node.left:
                node = node.left
            return node
        while node.parent and node.parent.right is node:
            node = node.parent
        return node.parent
