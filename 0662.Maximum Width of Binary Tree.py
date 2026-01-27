from collections import deque


class Solution:
    def widthOfBinaryTree(self, root: "TreeNode | None") -> int:
        """BFS with position indexing to compute maximum level width.

        Intuition:
        Assign position indices to nodes (left child = 2*i, right child = 2*i+1).
        The width of a level is the difference between the last and first positions + 1.

        Approach:
        1. Use BFS with a deque storing (node, position) pairs.
        2. At each level, compute width as last_position - first_position + 1.
        3. Track the maximum width across all levels.

        Complexity:
        Time: O(n)
        Space: O(n)
        """
        max_width = 0
        queue = deque([(root, 1)])
        while queue:
            max_width = max(max_width, queue[-1][1] - queue[0][1] + 1)
            for _ in range(len(queue)):
                node, position = queue.popleft()
                if node.left:
                    queue.append((node.left, position << 1))
                if node.right:
                    queue.append((node.right, position << 1 | 1))
        return max_width
