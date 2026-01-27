from math import inf


class TreeNode:
    def __init__(
        self,
        val: int = 0,
        left: "TreeNode | None" = None,
        right: "TreeNode | None" = None,
    ) -> None:
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxSumBST(self, root: TreeNode | None) -> int:
        """Find the maximum sum of all keys in any BST subtree.

        Intuition:
            Post-order traversal lets us validate BST property bottom-up while
            computing subtree sums, tracking the maximum valid BST sum.

        Approach:
            For each node, recursively obtain whether left and right subtrees
            are valid BSTs along with their min, max, and sum values. If the
            current subtree forms a valid BST, update the global maximum sum
            and propagate the combined info upward.

        Complexity:
            Time: O(n) where n is the number of nodes.
            Space: O(h) where h is the tree height.
        """

        def traverse(node: TreeNode | None) -> tuple[bool, float, float, int]:
            if node is None:
                return True, inf, -inf, 0

            left_valid, left_min, left_max, left_sum = traverse(node.left)
            right_valid, right_min, right_max, right_sum = traverse(node.right)

            if left_valid and right_valid and left_max < node.val < right_min:
                nonlocal max_sum
                subtree_sum = left_sum + right_sum + node.val
                max_sum = max(max_sum, subtree_sum)
                return (
                    True,
                    min(left_min, node.val),
                    max(right_max, node.val),
                    subtree_sum,
                )

            return False, 0, 0, 0

        max_sum = 0
        traverse(root)
        return max_sum
