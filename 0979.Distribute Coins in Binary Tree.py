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
    def distributeCoins(self, root: TreeNode | None) -> int:
        """Post-order DFS counting excess coins flowing through each edge.

        Intuition:
        Each subtree must end with exactly one coin per node. The excess or
        deficit at each node must flow through edges, and the total moves
        equals the sum of absolute flows across all edges.

        Approach:
        1. DFS returns the net coin excess of each subtree (coins - nodes)
        2. The moves through each edge equal the absolute value of that excess
        3. Accumulate absolute left and right excess at each node

        Complexity:
        Time: O(n) where n is the number of nodes
        Space: O(h) where h is the tree height for recursion stack
        """
        total_moves = 0

        def dfs(node: TreeNode | None) -> int:
            nonlocal total_moves
            if node is None:
                return 0
            left_excess = dfs(node.left)
            right_excess = dfs(node.right)
            total_moves += abs(left_excess) + abs(right_excess)
            return left_excess + right_excess + node.val - 1

        dfs(root)
        return total_moves
