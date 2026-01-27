from collections import deque


class Solution:
    def zigzagLevelOrder(self, root: TreeNode | None) -> list[list[int]]:
        """BFS with Alternating Direction

        Intuition:
            This is a level order traversal where odd-depth levels are read
            right-to-left. We can collect each level left-to-right and simply
            reverse the list for alternating levels.

        Approach:
            Use standard BFS with a deque. Track a boolean flag that toggles
            each level. Collect node values left-to-right, then reverse the
            list when the flag indicates a right-to-left level before appending
            to the result.

        Complexity:
            Time: O(n)
            Space: O(n)
        """
        result = []
        if root is None:
            return result
        queue = deque([root])
        is_left_to_right = True
        while queue:
            level_values = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level_values.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(level_values if is_left_to_right else level_values[::-1])
            is_left_to_right = not is_left_to_right
        return result
