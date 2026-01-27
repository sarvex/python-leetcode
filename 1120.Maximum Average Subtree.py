# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maximumAverageSubtree(self, root: TreeNode | None) -> float:
        """Find the maximum average value among all subtrees.

        Intuition:
            Each subtree's average can be computed from its sum and node count,
            both obtainable via a single post-order traversal.

        Approach:
            Use DFS to return (subtree_sum, node_count) for each node. At each
            node, compute the average and track the global maximum.

        Complexity:
            Time: O(n) where n is the number of nodes
            Space: O(h) where h is the height of the tree for recursion stack
        """
        max_average = 0.0

        def dfs(node: TreeNode | None) -> tuple[int, int]:
            nonlocal max_average
            if node is None:
                return 0, 0
            left_sum, left_count = dfs(node.left)
            right_sum, right_count = dfs(node.right)
            total_sum = node.val + left_sum + right_sum
            total_count = 1 + left_count + right_count
            max_average = max(max_average, total_sum / total_count)
            return total_sum, total_count

        dfs(root)
        return max_average
