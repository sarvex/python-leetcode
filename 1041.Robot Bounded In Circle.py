class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        """Robot Bounded In Circle via direction and displacement analysis.

        Intuition:
            After one cycle of instructions, the robot is bounded if it returns
            to the origin or is not facing north (it will return within 4 cycles).

        Approach:
            Track displacement in each of the 4 directions and the final
            facing direction. The robot is bounded if net displacement is zero
            in both axes, or the direction changed from north.

        Complexity:
            Time: O(n)
            Space: O(1)
        """
        direction = 0
        displacement = [0] * 4
        for instruction in instructions:
            if instruction == "L":
                direction = (direction + 1) % 4
            elif instruction == "R":
                direction = (direction + 3) % 4
            else:
                displacement[direction] += 1
        is_zero_displacement = (
            displacement[0] == displacement[2] and displacement[1] == displacement[3]
        )
        return is_zero_displacement or direction != 0
