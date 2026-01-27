class Solution:
    def swimInWater(self, grid: list[list[int]]) -> int:
        """Binary search on answer combined with DFS path validation.

        Intuition:
            The minimum time needed is at least the maximum of start and end values.
            We can binary search on possible time values and check if a path exists
            where all cells have values <= that time.

        Approach:
            1. Binary search on the time range [max(start, end), n*n-1]
            2. For each mid value, use DFS to check if we can reach destination
            3. Only visit cells with value <= current time threshold
            4. If reachable, try smaller times; otherwise try larger times

        Complexity:
            Time: O(n^2 * log(n^2)) where n is grid dimension
            Space: O(n^2) for visited set and recursion stack
        """
        size = len(grid)
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def dfs(
            row: int, col: int, max_time: int, visited: set[tuple[int, int]]
        ) -> bool:
            if row == size - 1 and col == size - 1:
                return True

            visited.add((row, col))

            for delta_row, delta_col in directions:
                new_row, new_col = delta_row + row, delta_col + col

                if (
                    0 <= new_row < size
                    and 0 <= new_col < size
                    and (new_row, new_col) not in visited
                    and grid[new_row][new_col] <= max_time
                ):
                    if dfs(new_row, new_col, max_time, visited):
                        return True

            return False

        low = max(grid[0][0], grid[size - 1][size - 1])
        high = size * size - 1
        result = high

        while low <= high:
            mid = (low + high) // 2
            visited: set[tuple[int, int]] = set()

            if dfs(0, 0, mid, visited):
                high = mid - 1
                result = mid
            else:
                low = mid + 1

        return result
