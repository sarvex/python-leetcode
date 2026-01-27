class Solution:
    def longestConsecutive(self, root: "TreeNode | None") -> int:
        """DFS tracking consecutive sequence length at each node.

        Intuition:
            At each node, check whether its children continue the consecutive
            sequence (value differs by exactly 1). Track the global maximum
            across all paths.

        Approach:
            1. Recursively compute the longest consecutive path starting from each node.
            2. If a child's value is exactly parent's value + 1, extend the path length.
            3. Otherwise, reset the path length to 1.
            4. Update the global answer with the maximum path at each node.

        Complexity:
            Time: O(n) where n is the number of nodes
            Space: O(h) where h is the height of the tree
        """
        longest = 0

        def dfs(node: "TreeNode | None") -> int:
            if node is None:
                return 0
            left_length = dfs(node.left) + 1
            right_length = dfs(node.right) + 1
            if node.left and node.left.val - node.val != 1:
                left_length = 1
            if node.right and node.right.val - node.val != 1:
                right_length = 1
            current_max = max(left_length, right_length)
            nonlocal longest
            longest = max(longest, current_max)
            return current_max

        dfs(root)
        return longest
