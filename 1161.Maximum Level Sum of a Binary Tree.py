from collections import deque
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        """BFS level-order traversal to find the level with maximum sum

        Intuition:
        Use BFS to traverse the tree level by level. Instead of a deque, use a simple list
        of current level nodes which is more Pythonic and efficient for level-order.

        Approach:
        1. Start with a list containing the root.
        2. While the current level has nodes:
           a. Calculate the sum of the current level.
           b. Update max_sum and max_level if current level sum is strictly greater.
           c. Generate the next level nodes from children of the current level.
        3. Return the max_level.

        Complexity:
        Time: O(n) where n is the number of nodes in the tree
        Space: O(w) where w is the maximum width of the tree
        """
        if not root:
            return 0

        max_sum, max_level = -float("inf"), 0
        current_level_nodes = [root]
        level_idx = 0

        while current_level_nodes:
            level_idx += 1
            current_sum = sum(node.val for node in current_level_nodes)

            if current_sum > max_sum:
                max_sum, max_level = current_sum, level_idx

            current_level_nodes = [
                child
                for node in current_level_nodes
                for child in (node.left, node.right)
                if child
            ]

        return max_level
