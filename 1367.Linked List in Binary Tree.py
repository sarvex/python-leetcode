class ListNode:
    def __init__(self, val: int = 0, next: "ListNode | None" = None) -> None:
        self.val = val
        self.next = next


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
    def isSubPath(self, head: ListNode | None, root: TreeNode | None) -> bool:
        """Check if a linked list is a downward path in a binary tree.

        Intuition:
            Try to match the linked list starting from every tree node. For
            each starting node, recursively check if the list matches along
            any downward path.

        Approach:
            Use two recursive functions: one to try each tree node as a
            starting point, and another to match the linked list along a
            path from a given tree node downward.

        Complexity:
            Time: O(n * min(l, h)) where n is tree nodes, l is list length, h is height.
            Space: O(h) for recursion stack.
        """

        def matches(list_node: ListNode | None, tree_node: TreeNode | None) -> bool:
            if list_node is None:
                return True
            if tree_node is None or tree_node.val != list_node.val:
                return False
            return matches(list_node.next, tree_node.left) or matches(
                list_node.next, tree_node.right
            )

        if root is None:
            return False
        return (
            matches(head, root)
            or self.isSubPath(head, root.left)
            or self.isSubPath(head, root.right)
        )
