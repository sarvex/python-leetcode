from collections import deque


class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        """BFS Level-by-Level Traversal

        Intuition:
            Level order traversal naturally maps to BFS. Process all nodes
            at the current depth before moving to the next level by tracking
            the queue size at each level.

        Approach:
            Use a deque as a queue initialized with the root. For each level,
            record the current queue size, then dequeue that many nodes while
            collecting their values and enqueuing their children. Append each
            level's values to the result.

        Complexity:
            Time: O(n)
            Space: O(n)
        """
        result = []
        if root is None:
            return result
        queue = deque([root])
        while queue:
            level_values = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level_values.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(level_values)
        return result
