class Solution:
    def judgeCircle(self, moves: str) -> bool:
        """Track x,y position and check if robot returns to origin.

        Intuition:
        Each move changes the position by one unit. The robot returns to origin
        if the net horizontal and vertical displacements are both zero.

        Approach:
        1. Initialize x and y coordinates to 0.
        2. For each move, update the appropriate coordinate.
        3. Return True if both coordinates are 0 after all moves.

        Complexity:
        Time: O(n)
        Space: O(1)
        """
        horizontal = vertical = 0
        for char in moves:
            if char == "R":
                horizontal += 1
            elif char == "L":
                horizontal -= 1
            elif char == "U":
                vertical += 1
            elif char == "D":
                vertical -= 1
        return horizontal == 0 and vertical == 0
