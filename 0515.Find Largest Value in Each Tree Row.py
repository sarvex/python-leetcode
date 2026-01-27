from collections import deque
from math import inf


class Solution:
    def largestValues(self, root: TreeNode | None) -> list[int]:
        """BFS level-order traversal tracking maximum value per level.

        Intuition:
            Traverse the tree level by level, keeping the maximum value
            encountered at each level.

        Approach:
            Use BFS with a queue. For each level, iterate through all nodes,
            track the maximum, and enqueue children.

        Complexity:
            Time: O(n)
            Space: O(n)
        """
        if root is None:
            return []
        queue = deque([root])
        result: list[int] = []
        while queue:
            level_max = -inf
            for _ in range(len(queue)):
                node = queue.popleft()
                level_max = max(level_max, node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(level_max)
        return result
