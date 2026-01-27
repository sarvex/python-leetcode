class TreeNode:
    def __init__(
        self,
        val: int = 0,
        left: "TreeNode | None" = None,
        right: "TreeNode | None" = None,
    ):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sufficientSubset(self, root: TreeNode | None, limit: int) -> TreeNode | None:
        """Remove nodes insufficient for any root-to-leaf path meeting limit.

        Intuition:
            A node is insufficient if all paths through it have sum < limit.
            Recursively prune from leaves upward.

        Approach:
            Subtract current node value from limit as we recurse. At leaves,
            remove if remaining limit > 0. At internal nodes, remove if both
            children are pruned.

        Complexity:
            Time: O(n) visiting each node once
            Space: O(h) for recursion stack where h is tree height
        """
        if root is None:
            return None
        limit -= root.val
        if root.left is None and root.right is None:
            return None if limit > 0 else root
        root.left = self.sufficientSubset(root.left, limit)
        root.right = self.sufficientSubset(root.right, limit)
        return None if root.left is None and root.right is None else root
