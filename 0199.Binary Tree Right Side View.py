from typing import List, Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        """BFS Level Order Traversal

        Intuition:
        When viewing a binary tree from the right side, we see the rightmost node at each level.
        This suggests a level-order traversal where we capture the last node at each level.

        Approach:
        1. Use BFS (level-order traversal) with a queue to process nodes level by level
        2. At each level, capture the value of the last node (rightmost node)
        3. Process all nodes at the current level and add their children to the queue

        Complexity:
        Time: O(n) where n is the number of nodes in the tree
        Space: O(w) where w is the maximum width of the tree (worst case O(n/2) ≈ O(n))
        """
        if not root:
            return []

        result = []
        queue = deque([root])

        while queue:
            size = len(queue)
            node = None

            # Process all nodes at current level
            for _ in range(size):
                node = queue.popleft()

                # Add children to queue for next level processing (left first, then right)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            # After processing the level, add the rightmost node's value
            result.append(node.val)

        return result
