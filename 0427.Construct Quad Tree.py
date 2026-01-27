class Solution:
    def construct(self, grid: list[list[int]]) -> "Node":
        """Recursive divide-and-conquer to build a quad tree from a grid.

        Intuition:
            If all values in a subgrid are the same, it becomes a leaf node.
            Otherwise, split into four quadrants and recurse.

        Approach:
            1. For the current subgrid, check if all values are 0 or all are 1.
            2. If uniform, return a leaf node with that value.
            3. Otherwise, split into top-left, top-right, bottom-left, bottom-right
               quadrants and recursively build each.
            4. Return a non-leaf node with the four children.

        Complexity:
            Time: O(n^2 * log n) where n is the grid dimension.
            Space: O(log n) for recursion depth.
        """

        def dfs(top: int, left: int, bottom: int, right: int) -> "Node":
            has_zero = has_one = 0
            for row in range(top, bottom + 1):
                for col in range(left, right + 1):
                    if grid[row][col] == 0:
                        has_zero = 1
                    else:
                        has_one = 1
            is_leaf = has_zero + has_one == 1
            value = is_leaf and has_one
            if is_leaf:
                return Node(grid[top][left], True)
            mid_row = (top + bottom) // 2
            mid_col = (left + right) // 2
            top_left = dfs(top, left, mid_row, mid_col)
            top_right = dfs(top, mid_col + 1, mid_row, right)
            bottom_left = dfs(mid_row + 1, left, bottom, mid_col)
            bottom_right = dfs(mid_row + 1, mid_col + 1, bottom, right)
            return Node(value, is_leaf, top_left, top_right, bottom_left, bottom_right)

        return dfs(0, 0, len(grid) - 1, len(grid[0]) - 1)
