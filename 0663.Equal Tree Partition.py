class Solution:
    def checkEqualTree(self, root: "TreeNode") -> bool:
        """DFS to compute subtree sums and check if half the total sum exists.

        Intuition:
        If we remove an edge, the tree splits into two parts. For equal partition,
        each part must have sum equal to half the total. Record all subtree sums
        and check if total/2 appears among non-root subtrees.

        Approach:
        1. DFS to compute and record every subtree sum.
        2. Check if the total sum is even.
        3. Verify that total_sum / 2 exists among non-root subtree sums.

        Complexity:
        Time: O(n)
        Space: O(n)
        """

        def compute_sum(node: "TreeNode | None") -> int:
            if node is None:
                return 0
            left_sum = compute_sum(node.left)
            right_sum = compute_sum(node.right)
            subtree_sums.append(left_sum + right_sum + node.val)
            return subtree_sums[-1]

        subtree_sums: list[int] = []
        total = compute_sum(root)
        if total % 2 == 1:
            return False
        subtree_sums.pop()
        return total // 2 in subtree_sums
