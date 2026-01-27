from collections import deque


class Solution:
    def levelOrder(self, root: "Node") -> list[list[int]]:
        """BFS level-order traversal of an N-ary tree.

        Intuition:
            Use a queue to process nodes level by level, collecting values
            at each depth before moving to the next.

        Approach:
            1. If root is None, return an empty list.
            2. Initialize a queue with the root node.
            3. For each level, dequeue all current nodes, record their values,
               and enqueue their children.
            4. Append each level's values to the result.

        Complexity:
            Time: O(n) where n is the number of nodes.
            Space: O(n) for the queue in the worst case.
        """
        result: list[list[int]] = []
        if root is None:
            return result
        queue = deque([root])
        while queue:
            level_values: list[int] = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level_values.append(node.val)
                queue.extend(node.children)
            result.append(level_values)
        return result
