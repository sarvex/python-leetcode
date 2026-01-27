class Solution:
    def isSameTree(self, p: TreeNode | None, q: TreeNode | None) -> bool:
        """Recursive Structural Comparison

        Intuition:
            Two trees are the same if their root values match and both their
            left and right subtrees are also the same. Base cases handle when
            both are None (same) or only one is None (different).

        Approach:
            Compare the two root nodes. If both are the same object (including
            both None), return True. If one is None or values differ, return
            False. Recursively check left and right subtrees.

        Complexity:
            Time: O(n)
            Space: O(n) for recursion stack
        """
        if p == q:
            return True
        if p is None or q is None or p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
