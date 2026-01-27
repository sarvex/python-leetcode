class Solution:
    def isSymmetric(self, root: TreeNode | None) -> bool:
        """Recursive Mirror Comparison

        Intuition:
            A tree is symmetric if the left subtree is a mirror reflection of
            the right subtree. Two subtrees mirror each other when their root
            values are equal, left of one matches right of the other, and
            vice versa.

        Approach:
            Define a helper that takes two nodes and checks if they are
            mirrors. Both None means symmetric at this level. One None or
            mismatched values means not symmetric. Recursively compare
            left-right and right-left pairs.

        Complexity:
            Time: O(n)
            Space: O(n) for recursion stack
        """

        def is_mirror(node1: TreeNode | None, node2: TreeNode | None) -> bool:
            if node1 is None and node2 is None:
                return True
            if node1 is None or node2 is None or node1.val != node2.val:
                return False
            return is_mirror(node1.left, node2.right) and is_mirror(
                node1.right, node2.left
            )

        return is_mirror(root, root)
