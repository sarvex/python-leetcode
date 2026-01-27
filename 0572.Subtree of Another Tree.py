class Solution:
    def isSubtree(self, root: "TreeNode", subRoot: "TreeNode") -> bool:
        """Check if one tree is a subtree of another using recursive matching.

        Intuition:
            A tree is a subtree if it exactly matches some subtree rooted at
            any node in the main tree. We check each node as a potential root.

        Approach:
            1. Define a helper that checks if two trees are identical.
            2. For each node in the main tree, check if the subtree rooted
               there matches subRoot.
            3. Recursively check left and right children.

        Complexity:
            Time: O(m * n) where m and n are node counts of each tree
            Space: O(h) where h is the height of the main tree
        """

        def is_same_tree(node1: "TreeNode | None", node2: "TreeNode | None") -> bool:
            if node1 is None and node2 is None:
                return True
            if node1 is None or node2 is None:
                return False
            return (
                node1.val == node2.val
                and is_same_tree(node1.left, node2.left)
                and is_same_tree(node1.right, node2.right)
            )

        if root is None:
            return False
        return (
            is_same_tree(root, subRoot)
            or self.isSubtree(root.left, subRoot)
            or self.isSubtree(root.right, subRoot)
        )
