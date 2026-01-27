class Solution:
    def findSecondMinimumValue(self, root: "TreeNode | None") -> int:
        """DFS to find second minimum value in a special binary tree.

        Intuition:
        The root holds the minimum value. DFS through the tree to find the smallest
        value strictly greater than the root value.

        Approach:
        1. Record the root value as the minimum.
        2. DFS through all nodes.
        3. For any node with value > root value, update the answer as the minimum
           such value found.
        4. Return -1 if no second minimum exists.

        Complexity:
        Time: O(n)
        Space: O(n) for recursion stack
        """

        def dfs(node: "TreeNode | None") -> None:
            if node:
                dfs(node.left)
                dfs(node.right)
                nonlocal second_min, min_val
                if node.val > min_val:
                    second_min = (
                        node.val if second_min == -1 else min(second_min, node.val)
                    )

        second_min, min_val = -1, root.val
        dfs(root)
        return second_min
