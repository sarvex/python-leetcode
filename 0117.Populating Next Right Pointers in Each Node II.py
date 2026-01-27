from collections import deque


class Node:
    def __init__(
        self,
        val: int = 0,
        left: "Node | None" = None,
        right: "Node | None" = None,
        next: "Node | None" = None,
    ):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: Node | None) -> Node | None:
        """Level-Order BFS Approach

        Intuition:
            Similar to the perfect binary tree version, but the tree may not be
            complete. BFS still works since it naturally processes nodes level by
            level regardless of tree shape.

        Approach:
            Use a queue for BFS. For each level, iterate through all nodes and link
            each node's next pointer to the following node in the same level.

        Complexity:
            Time: O(n) where n is the number of nodes
            Space: O(n) for the queue
        """
        if root is None:
            return root
        queue = deque([root])
        while queue:
            previous = None
            for _ in range(len(queue)):
                node = queue.popleft()
                if previous:
                    previous.next = node
                previous = node
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return root
