from math import inf


class Solution:
    def largestBSTSubtree(self, root: "TreeNode | None") -> int:
        """Post-order DFS tracking min, max, and size of BST subtrees.

        Intuition:
            For each node, check if the subtree rooted there is a valid BST by
            comparing the node's value against the max of its left subtree and
            the min of its right subtree.

        Approach:
            1. Perform post-order DFS returning (min_val, max_val, size) for
               each subtree.
            2. If the current node's value is between left max and right min,
               it forms a valid BST — update the global answer.
            3. Otherwise, return sentinel values to invalidate the subtree.

        Complexity:
            Time: O(n) where n is the number of nodes
            Space: O(h) where h is the height of the tree
        """

        def dfs(node: "TreeNode | None") -> tuple[float, float, int]:
            if node is None:
                return inf, -inf, 0
            left_min, left_max, left_size = dfs(node.left)
            right_min, right_max, right_size = dfs(node.right)
            nonlocal result
            if left_max < node.val < right_min:
                total_size = left_size + right_size + 1
                result = max(result, total_size)
                return min(left_min, node.val), max(right_max, node.val), total_size
            return -inf, inf, 0

        result = 0
        dfs(root)
        return result
