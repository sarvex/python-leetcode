class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
        """Recursive Construction with Index Mapping

        Intuition:
            The first element of preorder is always the root. Its position in
            inorder splits the tree into left and right subtrees. We can
            recursively build each subtree using these boundaries.

        Approach:
            Build a hash map from inorder values to their indices for O(1)
            lookup. Recursively construct the tree: the current root is
            preorder[i], find its position in inorder to determine left
            subtree size, then recurse for left and right subtrees with
            adjusted index ranges.

        Complexity:
            Time: O(n)
            Space: O(n)
        """

        def dfs(pre_start: int, in_start: int, size: int) -> TreeNode | None:
            if size <= 0:
                return None
            root_val = preorder[pre_start]
            inorder_idx = inorder_index_map[root_val]
            left_size = inorder_idx - in_start
            left = dfs(pre_start + 1, in_start, left_size)
            right = dfs(
                pre_start + 1 + left_size, inorder_idx + 1, size - left_size - 1
            )
            return TreeNode(root_val, left, right)

        inorder_index_map = {val: idx for idx, val in enumerate(inorder)}
        return dfs(0, 0, len(preorder))
