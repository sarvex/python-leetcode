class BSTIterator:
    """Iterator over a BST in ascending (inorder) order.

    Flattens the BST into a sorted list via inorder traversal at construction,
    then serves elements sequentially.
    """

    def __init__(self, root: TreeNode) -> None:
        """Initialize by performing a full inorder traversal.

        Intuition:
            Inorder traversal of a BST yields sorted values.

        Approach:
            Recursively traverse left, collect value, traverse right.

        Complexity:
            Time: O(n)
            Space: O(n)
        """

        def inorder(node: TreeNode | None) -> None:
            if node:
                inorder(node.left)
                self.values.append(node.val)
                inorder(node.right)

        self.cursor = 0
        self.values = []
        inorder(root)

    def next(self) -> int:
        """Return the next smallest element in the BST.

        Complexity:
            Time: O(1)
            Space: O(1)
        """
        result = self.values[self.cursor]
        self.cursor += 1
        return result

    def hasNext(self) -> bool:
        """Return whether there are remaining elements.

        Complexity:
            Time: O(1)
            Space: O(1)
        """
        return self.cursor < len(self.values)
