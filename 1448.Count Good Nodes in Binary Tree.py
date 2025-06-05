from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def goodNodes(self, root: Optional[TreeNode]) -> int:
        """DFS with path maximum tracking

        Intuition:
        A node is "good" if there are no nodes with greater values in the path from root to this node.
        This suggests we need to track the maximum value seen so far along each path.

        Approach:
        Perform a depth-first search while keeping track of the maximum value seen in the current path.
        For each node, compare its value with the current maximum. If it's greater or equal,
        it's a "good" node and we increment our counter.

        Complexity:
        Time: O(n) where n is the number of nodes in the tree
        Space: O(h) where h is the height of the tree (recursion stack)
        """
        def dfs(node: Optional[TreeNode], path_max: int) -> int:
            if not node:
                return 0

            # Check if current node is good (greater than or equal to path maximum)
            is_good = 1 if node.val >= path_max else 0

            # Update path maximum for children
            new_max = max(path_max, node.val)

            # Count good nodes in left and right subtrees
            left_count = dfs(node.left, new_max)
            right_count = dfs(node.right, new_max)

            return is_good + left_count + right_count

        return dfs(root, float('-inf'))
