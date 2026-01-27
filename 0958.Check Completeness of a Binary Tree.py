from collections import deque


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        """BFS level-order traversal checking no non-null node follows a null.

        Intuition:
            In a complete binary tree, all None nodes in BFS order must appear
            only at the end. Once we encounter a None, every subsequent node
            must also be None.

        Approach:
            1. Perform BFS, enqueueing both left and right children (including None).
            2. When a None node is dequeued, stop processing.
            3. Verify all remaining nodes in the queue are also None.

        Complexity:
            Time: O(n) — visit each node once
            Space: O(n) — queue holds up to one level of nodes
        """
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if node is None:
                break
            queue.append(node.left)
            queue.append(node.right)
        return all(node is None for node in queue)
