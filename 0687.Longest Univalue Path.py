class Solution:
    def longestUnivaluePath(self, root: TreeNode | None) -> int:
        """DFS to find the longest path of nodes with the same value.

        Intuition:
            For each node, the longest univalue path passing through it equals
            the sum of matching-value extensions from its left and right
            children. Track the global maximum across all nodes.

        Approach:
            1. DFS returns the longest single-direction univalue extension
               from the current node.
            2. If a child has the same value, extend by 1 + child's extension.
            3. Update the global answer with left + right extension at each node.

        Complexity:
            Time: O(n) visiting each node once
            Space: O(h) recursion depth where h is tree height
        """

        def dfs(node: TreeNode | None) -> int:
            if node is None:
                return 0
            left_length, right_length = dfs(node.left), dfs(node.right)
            left_length = (
                left_length + 1 if node.left and node.left.val == node.val else 0
            )
            right_length = (
                right_length + 1 if node.right and node.right.val == node.val else 0
            )
            nonlocal longest
            longest = max(longest, left_length + right_length)
            return max(left_length, right_length)

        longest = 0
        dfs(root)
        return longest
