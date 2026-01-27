# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def btreeGameWinningMove(self, root: TreeNode | None, n: int, x: int) -> bool:
        """Determine if the second player can guarantee a win.

        Intuition:
            The second player can choose a node adjacent to x, partitioning
            the tree into regions. The player wins if any region has more
            than half the nodes.

        Approach:
            Find node x, then count nodes in its left and right subtrees.
            The parent region has n - left - right - 1 nodes. The second
            player wins if the largest region exceeds n // 2.

        Complexity:
            Time: O(n) to find the node and count subtree sizes
            Space: O(h) where h is the height of the tree
        """

        def find_node(node: TreeNode | None) -> TreeNode | None:
            if node is None or node.val == x:
                return node
            return find_node(node.left) or find_node(node.right)

        def count_nodes(node: TreeNode | None) -> int:
            if node is None:
                return 0
            return 1 + count_nodes(node.left) + count_nodes(node.right)

        target = find_node(root)
        left_count = count_nodes(target.left)
        right_count = count_nodes(target.right)
        parent_count = n - left_count - right_count - 1
        return max(left_count, right_count, parent_count) > n // 2
