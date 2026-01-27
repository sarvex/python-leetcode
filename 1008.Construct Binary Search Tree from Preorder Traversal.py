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
    def bstFromPreorder(self, preorder: list[int]) -> TreeNode | None:
        """Construct a BST from its preorder traversal.

        Intuition:
            The first element is the root. All elements smaller go to the left
            subtree, all larger go to the right. Binary search finds the split.

        Approach:
            Recursively build the tree. Use binary search to find the partition
            point where values exceed the root, then recurse on both halves.

        Complexity:
            Time: O(n log n) average with binary search at each level
            Space: O(n) for recursion and array slicing
        """

        def build(values: list[int]) -> TreeNode | None:
            if not values:
                return None
            root = TreeNode(values[0])
            left, right = 1, len(values)
            while left < right:
                mid = (left + right) >> 1
                if values[mid] > values[0]:
                    right = mid
                else:
                    left = mid + 1
            root.left = build(values[1:left])
            root.right = build(values[left:])
            return root

        return build(preorder)
