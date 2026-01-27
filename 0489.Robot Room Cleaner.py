class Solution:
    def cleanRoom(self, robot) -> None:
        """DFS backtracking with direction tracking for room cleaning.

        Intuition:
            Explore the room using DFS, tracking visited cells. When
            backtracking, reverse the robot's movement to return to the
            previous cell.

        Approach:
            Use a set to track visited positions. From each cell, try all
            four directions. If the next cell is unvisited and reachable,
            recurse into it. After exploring, turn the robot around, move
            back, and turn around again to restore orientation. Rotate
            right to try the next direction.

        Complexity:
            Time: O(n - m) where n is total cells, m is obstacles
            Space: O(n - m) for the visited set
        """

        def dfs(row: int, col: int, direction: int) -> None:
            visited.add((row, col))
            robot.clean()
            for k in range(4):
                new_direction = (direction + k) % 4
                new_row, new_col = (
                    row + directions[new_direction],
                    col + directions[new_direction + 1],
                )
                if (new_row, new_col) not in visited and robot.move():
                    dfs(new_row, new_col, new_direction)
                    robot.turnRight()
                    robot.turnRight()
                    robot.move()
                    robot.turnRight()
                    robot.turnRight()
                robot.turnRight()

        directions = (-1, 0, 1, 0, -1)
        visited: set[tuple[int, int]] = set()
        dfs(0, 0, 0)
