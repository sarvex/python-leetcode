from functools import cache


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> list[TreeNode | None]:
        """Memoized recursion generating all full binary trees with n nodes.

        Intuition:
            A full binary tree with n nodes has a root and two subtrees
            whose sizes sum to n-1. Enumerate all valid left/right splits.

        Approach:
            1. Base case: n=1 yields a single leaf node.
            2. For each split of n-1 nodes into left and right subtrees,
               combine all possible left trees with all possible right trees.
            3. Memoize results for each n.

        Complexity:
            Time: O(2^(n/2)) — Catalan number growth.
            Space: O(n * 2^(n/2))
        """

        @cache
        def dfs(node_count: int) -> list[TreeNode | None]:
            if node_count == 1:
                return [TreeNode()]
            result: list[TreeNode | None] = []
            for left_count in range(node_count - 1):
                right_count = node_count - 1 - left_count
                for left_tree in dfs(left_count):
                    for right_tree in dfs(right_count):
                        result.append(TreeNode(0, left_tree, right_tree))
            return result

        return dfs(n)
