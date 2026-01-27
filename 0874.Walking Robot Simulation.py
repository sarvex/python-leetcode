class Solution:
    def robotSim(self, commands: list[int], obstacles: list[list[int]]) -> int:
        """Simulation with direction vectors and obstacle hash set.

        Intuition:
            Simulate the robot's movement step by step, using a set of
            obstacles for O(1) collision checks and direction vectors
            for turning.

        Approach:
            1. Store obstacles in a set for fast lookup.
            2. Use direction vectors (N, E, S, W) indexed by a direction state.
            3. Process each command: turn left/right adjusts direction,
               move forward checks each step against obstacles.
            4. Track the maximum Euclidean distance squared from origin.

        Complexity:
            Time: O(n * max_step + m) where n is commands length, m is obstacles count.
            Space: O(m)
        """
        directions = (0, 1, 0, -1, 0)
        obstacle_set = {(x, y) for x, y in obstacles}
        max_distance = 0
        direction_index = 0
        pos_x = pos_y = 0
        for command in commands:
            if command == -2:
                direction_index = (direction_index + 3) % 4
            elif command == -1:
                direction_index = (direction_index + 1) % 4
            else:
                for _ in range(command):
                    next_x = pos_x + directions[direction_index]
                    next_y = pos_y + directions[direction_index + 1]
                    if (next_x, next_y) in obstacle_set:
                        break
                    pos_x, pos_y = next_x, next_y
                    max_distance = max(max_distance, pos_x * pos_x + pos_y * pos_y)
        return max_distance
