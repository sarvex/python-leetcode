class TreeNode:
    def __init__(
        self,
        val: int = 0,
        left: "TreeNode | None" = None,
        right: "TreeNode | None" = None,
    ):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def twoSumBSTs(
        self, root1: TreeNode | None, root2: TreeNode | None, target: int
    ) -> bool:
        """Two sum across two BSTs using two-pointer technique.

        Intuition:
            Perform inorder traversal on both BSTs to get sorted arrays, then
            use a two-pointer approach to find a pair summing to target.

        Approach:
            Collect sorted values from both trees via inorder DFS. Use a left
            pointer on the first array and a right pointer on the second to
            efficiently search for the target sum.

        Complexity:
            Time: O(n + m) where n and m are the sizes of the two trees
            Space: O(n + m) for storing the sorted values
        """

        def inorder(root: TreeNode | None, values: list[int]) -> None:
            if root is None:
                return
            inorder(root.left, values)
            values.append(root.val)
            inorder(root.right, values)

        values1: list[int] = []
        values2: list[int] = []
        inorder(root1, values1)
        inorder(root2, values2)
        left, right = 0, len(values2) - 1
        while left < len(values1) and right >= 0:
            total = values1[left] + values2[right]
            if total == target:
                return True
            if total < target:
                left += 1
            else:
                right -= 1
        return False
