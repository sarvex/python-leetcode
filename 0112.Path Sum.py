class Solution:
    def hasPathSum(self, root: TreeNode | None, targetSum: int) -> bool:
        """DFS with Running Sum

        Intuition:
            Accumulate the sum along each root-to-leaf path. At each leaf,
            check if the accumulated sum equals the target.

        Approach:
            Use a recursive DFS that carries the running sum. Add the current
            node's value to the sum. If the node is a leaf and the sum matches
            the target, return True. Otherwise recurse into left and right
            children, returning True if either path succeeds.

        Complexity:
            Time: O(n)
            Space: O(n) for recursion stack
        """

        def dfs(node: TreeNode | None, current_sum: int) -> bool:
            if node is None:
                return False
            current_sum += node.val
            if node.left is None and node.right is None and current_sum == targetSum:
                return True
            return dfs(node.left, current_sum) or dfs(node.right, current_sum)

        return dfs(root, 0)
