from collections import deque


class TreeNode:
    def __init__(
        self,
        val: int = 0,
        left: "TreeNode | None" = None,
        right: "TreeNode | None" = None,
    ):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isCousins(self, root: TreeNode | None, x: int, y: int) -> bool:
        """Determine if two nodes are cousins (same depth, different parents).

        Intuition:
            BFS level by level tracks both depth and parent naturally. Two nodes
            are cousins when found at the same depth with different parents.

        Approach:
            Perform BFS storing each node with its parent. Record the parent and
            depth when x or y is found, then compare after traversal.

        Complexity:
            Time: O(n) visiting every node once
            Space: O(n) for the BFS queue
        """
        queue: deque[tuple[TreeNode, TreeNode | None]] = deque([(root, None)])
        depth = 0
        parent_x = parent_y = None
        depth_x = depth_y = None
        while queue:
            for _ in range(len(queue)):
                node, parent = queue.popleft()
                if node.val == x:
                    parent_x, depth_x = parent, depth
                elif node.val == y:
                    parent_y, depth_y = parent, depth
                if node.left:
                    queue.append((node.left, node))
                if node.right:
                    queue.append((node.right, node))
            depth += 1
        return parent_x != parent_y and depth_x == depth_y
