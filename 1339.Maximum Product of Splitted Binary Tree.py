import sys

sys.setrecursionlimit(100000)


class Solution:
    def maxProduct(self, root: TreeNode | None) -> int:
        """Maximize the product of sums of two subtrees after removing one edge.

        Intuition:
            Removing an edge splits the tree into two parts. The product is
            subtree_sum * (total - subtree_sum). Maximize over all edges.

        Approach:
            First DFS to compute the total sum while collecting all subtree sums.
            Then find the subtree sum that maximizes s * (total - s).

        Complexity:
            Time: O(n)
            Space: O(n)
        """
        subtree_sums: list[int] = []

        def dfs(node: TreeNode | None) -> int:
            if not node:
                return 0
            total = node.val + dfs(node.left) + dfs(node.right)
            subtree_sums.append(total)
            return total

        tree_total = dfs(root)
        return max(s * (tree_total - s) for s in subtree_sums) % (10**9 + 7)
