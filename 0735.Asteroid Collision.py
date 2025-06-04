from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        """Stack-based simulation of asteroid collisions with optimized while-else pattern.

        Intuition: Use a stack to track asteroids moving to the right (positive values).
        When encountering a leftward asteroid (negative value), simulate collisions with
        existing rightward asteroids on the stack.

        Approach:
        1. Maintain a stack to track surviving asteroids
        2. For each asteroid:
           - Use a while loop to handle collisions with rightward asteroids
           - Use the while-else pattern to add the asteroid only if it survives all collisions
           - Break early if the current asteroid is destroyed
        3. Return the final stack as the result

        Complexity:
        Time: O(n) where n is the number of asteroids
        Space: O(n) for the stack in worst case
        """
        stack = []

        for asteroid in asteroids:
            while stack and stack[-1] > 0 and asteroid < 0:
                if abs(stack[-1]) > abs(asteroid):
                    break
                elif abs(stack[-1]) < abs(asteroid):
                    stack.pop()
                else:
                    stack.pop()
                    break
            else:
                stack.append(asteroid)

        return stack
