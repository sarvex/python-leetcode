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
        Use BFS to traverse the tree level by level, calculating the sum at each level.
        Track the maximum sum and its corresponding level.

        Approach:
        1. Use a queue for level-order traversal
        2. Process nodes level by level, calculating sum for each level
        3. Track the maximum sum and its level
        4. Return the level with the maximum sum

        Complexity:
        Time: O(n) where n is the number of nodes in the tree
        Space: O(w) where w is the maximum width of the tree
        """
        if not root:
            return 0

        queue = deque([root])
        max_sum = -float('inf')
        max_level = 0
        current_level = 0

        while queue:
            current_level += 1
            level_size = len(queue)
            level_sum = 0

            # Process all nodes at current level
            for _ in range(level_size):
                node = queue.popleft()
                level_sum += node.val

                # Add children to queue for next level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            # Update max sum and level if current level has higher sum
            if level_sum > max_sum:
                max_sum = level_sum
                max_level = current_level

        return max_level
