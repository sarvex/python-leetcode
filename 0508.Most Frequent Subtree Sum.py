from collections import Counter


class Solution:
    def findFrequentTreeSum(self, root: TreeNode) -> list[int]:
        """DFS to compute subtree sums and find the most frequent ones.

        Intuition:
            Compute the subtree sum at every node using post-order DFS, then
            find which sums appear most frequently.

        Approach:
            Use DFS to compute each subtree sum and count occurrences with a
            Counter. Return all sums with the maximum frequency.

        Complexity:
            Time: O(n)
            Space: O(n)
        """

        def dfs(node: TreeNode | None) -> int:
            if node is None:
                return 0
            left_sum, right_sum = dfs(node.left), dfs(node.right)
            subtree_sum = node.val + left_sum + right_sum
            frequency[subtree_sum] += 1
            return subtree_sum

        frequency: Counter = Counter()
        dfs(root)
        max_freq = max(frequency.values())
        return [key for key, value in frequency.items() if value == max_freq]
