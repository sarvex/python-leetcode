class Solution:
    def pathSum(self, root: TreeNode | None, targetSum: int) -> list[list[int]]:
        """DFS Backtracking to Collect All Paths

        Intuition:
            Similar to Path Sum, but we need to collect all root-to-leaf paths
            that sum to the target. Use backtracking to build and dismantle
            the current path as we explore.

        Approach:
            Maintain a running path list and sum. At each node, append the
            value and update the sum. If a leaf matches the target, save a
            copy of the path. Recurse into both children, then pop the last
            value to backtrack.

        Complexity:
            Time: O(n^2) in worst case for copying paths
            Space: O(n) for recursion stack and current path
        """

        def dfs(node: TreeNode | None, current_sum: int) -> None:
            if node is None:
                return
            current_sum += node.val
            current_path.append(node.val)
            if node.left is None and node.right is None and current_sum == targetSum:
                result.append(current_path[:])
            dfs(node.left, current_sum)
            dfs(node.right, current_sum)
            current_path.pop()

        result: list[list[int]] = []
        current_path: list[int] = []
        dfs(root, 0)
        return result
