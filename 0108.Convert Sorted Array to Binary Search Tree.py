class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> TreeNode | None:
        """Recursive mid-point partitioning to build a height-balanced BST.

        Intuition:
            A sorted array's middle element is the ideal root for a balanced BST.
            Recursively applying this to left and right halves produces a
            height-balanced tree.

        Approach:
            1. Define a recursive helper with left and right bounds.
            2. Base case: left > right returns None.
            3. Pick the middle index as root.
            4. Recursively build left subtree from left half, right from right half.

        Complexity:
            Time: O(n)
            Space: O(log n) — recursion stack for balanced tree
        """

        def dfs(left: int, right: int) -> TreeNode | None:
            if left > right:
                return None
            mid = (left + right) >> 1
            left_child = dfs(left, mid - 1)
            right_child = dfs(mid + 1, right)
            return TreeNode(nums[mid], left_child, right_child)

        return dfs(0, len(nums) - 1)
