class Solution:
    def buildTree(self, inorder: list[int], postorder: list[int]) -> TreeNode | None:
        """Recursive construction using index mapping on inorder traversal.

        Intuition:
            The last element of postorder is the root. Finding that root in the
            inorder array splits it into left and right subtrees. We can recurse
            on each subtree using offset arithmetic to locate the corresponding
            postorder segments.

        Approach:
            1. Build a value-to-index map for the inorder array.
            2. Define a recursive helper that takes the inorder start index,
               postorder start index, and subtree size.
            3. The root is the last element in the current postorder segment.
            4. Use the inorder index of the root to determine left/right sizes.
            5. Recursively build left and right subtrees.

        Complexity:
            Time: O(n)
            Space: O(n)
        """

        def dfs(inorder_start: int, postorder_start: int, size: int) -> TreeNode | None:
            if size <= 0:
                return None
            root_val = postorder[postorder_start + size - 1]
            inorder_idx = index_map[root_val]
            left_size = inorder_idx - inorder_start
            left = dfs(inorder_start, postorder_start, left_size)
            right = dfs(
                inorder_idx + 1, postorder_start + left_size, size - left_size - 1
            )
            return TreeNode(root_val, left, right)

        index_map = {val: idx for idx, val in enumerate(inorder)}
        return dfs(0, 0, len(inorder))
