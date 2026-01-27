class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        """Sum values of nodes whose grandparent has an even value.

        Intuition:
            Pass the parent value down during DFS; when the grandparent (parent
            of current parent) is even, add grandchildren values.

        Approach:
            DFS with parent value parameter. If the parent value is even, add
            the current node's children values to the running sum.

        Complexity:
            Time: O(n)
            Space: O(h) where h is the tree height
        """

        def dfs(node: TreeNode | None, parent_val: int) -> int:
            if node is None:
                return 0
            total = dfs(node.left, node.val) + dfs(node.right, node.val)
            if parent_val % 2 == 0:
                if node.left:
                    total += node.left.val
                if node.right:
                    total += node.right.val
            return total

        return dfs(root, 1)
