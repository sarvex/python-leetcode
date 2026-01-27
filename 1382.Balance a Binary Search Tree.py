class TreeNode:
    def __init__(
        self,
        val: int = 0,
        left: "TreeNode | None" = None,
        right: "TreeNode | None" = None,
    ) -> None:
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        """Balance a binary search tree.

        Intuition:
            An inorder traversal of a BST yields sorted values. Rebuilding
            the tree by always choosing the middle element as root produces
            a balanced BST.

        Approach:
            Perform inorder traversal to collect sorted values. Recursively
            build a balanced BST by picking the middle element as the root
            at each level.

        Complexity:
            Time: O(n)
            Space: O(n)
        """

        def inorder(node: TreeNode | None) -> None:
            if node is None:
                return
            inorder(node.left)
            sorted_values.append(node.val)
            inorder(node.right)

        def build(left: int, right: int) -> TreeNode | None:
            if left > right:
                return None
            mid = (left + right) >> 1
            left_subtree = build(left, mid - 1)
            right_subtree = build(mid + 1, right)
            return TreeNode(sorted_values[mid], left_subtree, right_subtree)

        sorted_values: list[int] = []
        inorder(root)
        return build(0, len(sorted_values) - 1)
