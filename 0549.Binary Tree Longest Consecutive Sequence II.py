class Solution:
    def longestConsecutive(self, root: "TreeNode") -> int:
        """DFS tracking increasing and decreasing lengths at each node.

        Intuition:
            At each node, the longest consecutive path could go through it by
            combining an increasing path from one child with a decreasing path
            from the other child.

        Approach:
            1. DFS returns (increasing_length, decreasing_length) for each node.
            2. If a child's value is one less than current, extend the increasing chain.
            3. If a child's value is one more than current, extend the decreasing chain.
            4. Update the global answer with increasing + decreasing - 1 at each node.

        Complexity:
            Time: O(n)
            Space: O(h) where h is the height of the tree
        """

        def dfs(node: "TreeNode | None") -> list[int]:
            if node is None:
                return [0, 0]
            nonlocal answer
            increasing = decreasing = 1
            left_inc, left_dec = dfs(node.left)
            right_inc, right_dec = dfs(node.right)
            if node.left:
                if node.left.val + 1 == node.val:
                    increasing = left_inc + 1
                if node.left.val - 1 == node.val:
                    decreasing = left_dec + 1
            if node.right:
                if node.right.val + 1 == node.val:
                    increasing = max(increasing, right_inc + 1)
                if node.right.val - 1 == node.val:
                    decreasing = max(decreasing, right_dec + 1)
            answer = max(answer, increasing + decreasing - 1)
            return [increasing, decreasing]

        answer = 0
        dfs(root)
        return answer
