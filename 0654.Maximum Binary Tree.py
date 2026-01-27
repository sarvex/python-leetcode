class Solution:
    def constructMaximumBinaryTree(self, nums: list[int]) -> "TreeNode | None":
        """Recursive construction by finding max element and splitting array.

        Intuition:
        The root is always the maximum element. The left subtree is built from
        elements before the max, and the right subtree from elements after it.

        Approach:
        1. If the array is empty, return None.
        2. Find the maximum value and its index.
        3. Create a node with the max value.
        4. Recursively build left subtree from elements before the max.
        5. Recursively build right subtree from elements after the max.

        Complexity:
        Time: O(n^2) worst case, O(n log n) average
        Space: O(n)
        """

        def dfs(elements: list[int]) -> "TreeNode | None":
            if not elements:
                return None
            max_val = max(elements)
            max_idx = elements.index(max_val)
            root = TreeNode(max_val)
            root.left = dfs(elements[:max_idx])
            root.right = dfs(elements[max_idx + 1 :])
            return root

        return dfs(nums)
