from math import inf


class Codec:
    """Serialize and deserialize a BST using preorder traversal with value bounds."""

    def serialize(self, root: "TreeNode | None") -> str:
        """Encode a BST to a space-separated preorder string.

        Intuition:
            Preorder traversal uniquely defines a BST since BST property
            constrains the reconstruction.

        Approach:
            1. Perform preorder DFS, collecting node values.
            2. Join values as a space-separated string.

        Complexity:
            Time: O(n) for traversal.
            Space: O(n) for the values list.
        """

        def dfs(node: "TreeNode | None") -> None:
            if node is None:
                return
            values.append(node.val)
            dfs(node.left)
            dfs(node.right)

        values: list[int] = []
        dfs(root)
        return " ".join(map(str, values))

    def deserialize(self, data: str) -> "TreeNode | None":
        """Decode a preorder string back to a BST using value bounds.

        Intuition:
            Using min/max bounds, each value in the preorder sequence can be
            placed correctly without explicit null markers.

        Approach:
            1. Parse the string into a list of integers.
            2. Recursively build the tree: if the current value is within
               [min_val, max_val], create a node and recurse for left and right
               subtrees with updated bounds.

        Complexity:
            Time: O(n) for reconstruction.
            Space: O(n) for recursion stack.
        """

        def dfs(min_val: float, max_val: float) -> "TreeNode | None":
            nonlocal index
            if index == len(values) or not min_val <= values[index] <= max_val:
                return None
            value = values[index]
            root = TreeNode(value)
            index += 1
            root.left = dfs(min_val, value)
            root.right = dfs(value, max_val)
            return root

        values = list(map(int, data.split()))
        index = 0
        return dfs(-inf, inf)
