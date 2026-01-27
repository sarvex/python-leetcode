class Solution:
    def isBalanced(self, root: TreeNode | None) -> bool:
        """Bottom-Up Height Check

        Intuition:
            A balanced tree requires every subtree to have left and right
            heights differing by at most 1. We can check this bottom-up by
            computing heights and using -1 as a sentinel for imbalance.

        Approach:
            Define a recursive height function that returns the height of a
            subtree, or -1 if any subtree is unbalanced. At each node, compute
            left and right heights. If either is -1 or their difference exceeds
            1, propagate -1 upward. The tree is balanced if the final result
            is non-negative.

        Complexity:
            Time: O(n)
            Space: O(n) for recursion stack
        """

        def height(node: TreeNode | None) -> int:
            if node is None:
                return 0
            left_height, right_height = height(node.left), height(node.right)
            if (
                left_height == -1
                or right_height == -1
                or abs(left_height - right_height) > 1
            ):
                return -1
            return 1 + max(left_height, right_height)

        return height(root) >= 0
