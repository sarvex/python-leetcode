class Solution:
    def printTree(self, root: "TreeNode | None") -> list[list[str]]:
        """DFS to compute tree height and place values in a grid layout.

        Intuition:
        First determine the tree height to compute grid dimensions. Then place
        each node value at its correct row and column using DFS with offsets.

        Approach:
        1. Compute tree height using recursive DFS.
        2. Create a grid of (height+1) rows and (2^(height+1) - 1) columns.
        3. Place root at the center column of the first row.
        4. For each node, place children offset by 2^(height - row - 1).

        Complexity:
        Time: O(n)
        Space: O(2^h * h) for the output grid
        """

        def height(node: "TreeNode | None") -> int:
            if node is None:
                return -1
            return 1 + max(height(node.left), height(node.right))

        def dfs(node: "TreeNode | None", row: int, col: int) -> None:
            if node is None:
                return
            grid[row][col] = str(node.val)
            dfs(node.left, row + 1, col - 2 ** (tree_height - row - 1))
            dfs(node.right, row + 1, col + 2 ** (tree_height - row - 1))

        tree_height = height(root)
        rows, cols = tree_height + 1, 2 ** (tree_height + 1) - 1
        grid = [[""] * cols for _ in range(rows)]
        dfs(root, 0, (cols - 1) // 2)
        return grid
