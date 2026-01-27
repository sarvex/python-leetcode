from typing import Optional


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
    def findLeaves(self, root: TreeNode | None) -> list[list[int]]:
        """Collect leaves level by level using node height computation via DFS.

        Intuition:
            Each node belongs to the group corresponding to its height in the
            tree. Leaves have height 0, their parents have height 1, etc.

        Approach:
            Perform post-order DFS to compute the height of each node. Use the
            height as an index into the result list, appending the node's value
            to the corresponding group. Expand the result list as needed when
            encountering new height levels.

        Complexity:
            Time: O(n)
            Space: O(n)
        """

        def dfs(node: TreeNode | None) -> int:
            if node is None:
                return 0
            left_height = dfs(node.left)
            right_height = dfs(node.right)
            height = max(left_height, right_height)
            if len(result) == height:
                result.append([])
            result[height].append(node.val)
            return height + 1

        result: list[list[int]] = []
        dfs(root)
        return result
