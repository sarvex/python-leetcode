# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def pseudoPalindromicPaths(self, root: TreeNode | None) -> int:
        """Count root-to-leaf paths that can form a palindrome.

        Intuition:
            A path is pseudo-palindromic if at most one digit has an odd
            frequency, which can be tracked with a bitmask XOR.

        Approach:
            DFS through the tree toggling bits in a bitmask for each node
            value. At a leaf, check if the bitmask has at most one bit set
            (meaning at most one odd-frequency digit).

        Complexity:
            Time: O(n) visiting each node once
            Space: O(h) for recursion stack depth
        """

        def dfs(node: TreeNode | None, digit_mask: int) -> int:
            if node is None:
                return 0
            digit_mask ^= 1 << node.val
            if node.left is None and node.right is None:
                return int((digit_mask & (digit_mask - 1)) == 0)
            return dfs(node.left, digit_mask) + dfs(node.right, digit_mask)

        return dfs(root, 0)
