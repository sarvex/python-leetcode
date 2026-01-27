from collections import deque


class Solution:
    def findBottomLeftValue(self, root: TreeNode | None) -> int:
        """BFS level-order traversal to find the leftmost value in the last row.

        Intuition:
            The bottom-left value is the first node of the last level in a
            level-order traversal.

        Approach:
            Perform BFS. At the start of each level, record the first node's
            value. After traversal completes, the last recorded value is the answer.

        Complexity:
            Time: O(n)
            Space: O(n)
        """
        queue = deque([root])
        result = 0
        while queue:
            result = queue[0].val
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return result
