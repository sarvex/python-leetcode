from collections import deque


class TreeNode:
    def __init__(
        self,
        val: int = 0,
        left: "TreeNode | None" = None,
        right: "TreeNode | None" = None,
    ) -> None:
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deepestLeavesSum(self, root: TreeNode | None) -> int:
        """Sum of values of the deepest leaves in a binary tree.

        Intuition:
            BFS level by level; the sum of the last level processed is the answer.

        Approach:
            Use a queue for BFS. For each level, sum all node values. After the
            traversal completes, the last computed sum is the deepest leaves sum.

        Complexity:
            Time: O(n)
            Space: O(n)
        """
        queue = deque([root])
        level_sum = 0
        while queue:
            level_sum = 0
            for _ in range(len(queue)):
                node = queue.popleft()
                level_sum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return level_sum
