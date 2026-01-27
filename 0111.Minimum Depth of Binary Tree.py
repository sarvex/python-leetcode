class Solution:
    def minDepth(self, root: TreeNode | None) -> int:
        """Recursive Depth Calculation

        Intuition:
            Minimum depth is the shortest path from root to the nearest leaf.
            A key subtlety is that if one child is None, we must follow the
            other child rather than treating the None side as depth 0.

        Approach:
            Handle three cases recursively: if the node is None, return 0.
            If the left child is None, recurse only on the right. If the
            right child is None, recurse only on the left. Otherwise, take
            the minimum of both sides plus one.

        Complexity:
            Time: O(n)
            Space: O(n) for recursion stack
        """
        if root is None:
            return 0
        if root.left is None:
            return 1 + self.minDepth(root.right)
        if root.right is None:
            return 1 + self.minDepth(root.left)
        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))
