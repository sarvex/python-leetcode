from collections import deque


class Solution:
    def averageOfLevels(self, root: "TreeNode | None") -> list[float]:
        """BFS level-order traversal computing average value per level.

        Intuition:
        Traverse the tree level by level using BFS, summing node values at each
        level and dividing by the count of nodes.

        Approach:
        1. Use a deque for BFS starting from the root.
        2. At each level, process all nodes, summing their values.
        3. Compute the average and append to results.
        4. Enqueue children for the next level.

        Complexity:
        Time: O(n)
        Space: O(n)
        """
        queue = deque([root])
        averages = []
        while queue:
            level_sum, level_size = 0, len(queue)
            for _ in range(level_size):
                node = queue.popleft()
                level_sum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            averages.append(level_sum / level_size)
        return averages
