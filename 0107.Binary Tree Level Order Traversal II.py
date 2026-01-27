from collections import deque


class Solution:
    def levelOrderBottom(self, root: TreeNode | None) -> list[list[int]]:
        """BFS level order traversal with result reversal.

        Intuition:
            A standard BFS collects nodes level by level from top to bottom.
            Reversing the result gives bottom-up level order.

        Approach:
            1. Return empty list if root is None.
            2. Use a deque for BFS, processing one level at a time.
            3. Collect each level's values into a list.
            4. Reverse the final result before returning.

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
        return result[::-1]
