# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(
        self, preorder: list[int], postorder: list[int]
    ) -> TreeNode | None:
        """Recursive construction using preorder-postorder index mapping.

        Intuition:
            The first element of preorder is the root. The second element
            is the root of the left subtree. Find it in postorder to
            determine the boundary between left and right subtrees.

        Approach:
            1. Build a value-to-index map for postorder.
            2. Recursively construct trees using index ranges in both arrays.
            3. The left subtree size is determined by the position of
               preorder[pre_start+1] in postorder.

        Complexity:
            Time: O(n)
            Space: O(n)
        """

        def dfs(
            pre_start: int, pre_end: int, post_start: int, post_end: int
        ) -> TreeNode | None:
            if pre_start > pre_end:
                return None
            root = TreeNode(preorder[pre_start])
            if pre_start == pre_end:
                return root
            left_root_post_index = post_index[preorder[pre_start + 1]]
            left_size = left_root_post_index - post_start + 1
            root.left = dfs(
                pre_start + 1, pre_start + left_size, post_start, left_root_post_index
            )
            root.right = dfs(
                pre_start + left_size + 1,
                pre_end,
                left_root_post_index + 1,
                post_end - 1,
            )
            return root

        post_index = {value: index for index, value in enumerate(postorder)}
        return dfs(0, len(preorder) - 1, 0, len(postorder) - 1)
