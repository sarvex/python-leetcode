import math
import random


class Solution:
    """Generate uniformly random points inside a circle.

    Intuition:
        Uniform distribution in a circle requires sampling the radius with
        a square-root transformation to avoid clustering at the center.

    Approach:
        Generate a random radius using sqrt of a uniform [0, r^2] value and
        a random angle in [0, 2*pi). Convert polar coordinates to Cartesian
        and offset by the center.

    Complexity:
        Time: O(1) per call
        Space: O(1)
    """

    def __init__(self, radius: float, x_center: float, y_center: float) -> None:
        self.radius = radius
        self.x_center = x_center
        self.y_center = y_center

    def randPoint(self) -> list[float]:
        length = math.sqrt(random.uniform(0, self.radius**2))
        degree = random.uniform(0, 1) * 2 * math.pi
        x = self.x_center + length * math.cos(degree)
        y = self.y_center + length * math.sin(degree)
        return [x, y]
