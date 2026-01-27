class Solution:
    def findTilt(self, root: "TreeNode") -> int:
        """Compute total tilt of a binary tree using post-order traversal.

        Intuition:
            The tilt of a node is the absolute difference between the sum of
            its left subtree and the sum of its right subtree. We accumulate
            tilt while computing subtree sums bottom-up.

        Approach:
            1. Post-order DFS computes the subtree sum for each node.
            2. At each node, add |left_sum - right_sum| to the total tilt.
            3. Return the subtree sum (val + left_sum + right_sum) upward.

        Complexity:
            Time: O(n)
            Space: O(h) where h is the height of the tree
        """
        answer = 0

        def subtree_sum(node: "TreeNode | None") -> int:
            if node is None:
                return 0
            nonlocal answer
            left_sum = subtree_sum(node.left)
            right_sum = subtree_sum(node.right)
            answer += abs(left_sum - right_sum)
            return node.val + left_sum + right_sum

        subtree_sum(root)
        return answer
