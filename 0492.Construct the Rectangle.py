from math import sqrt


class Solution:
    def constructRectangle(self, area: int) -> list[int]:
        """Find closest factor pair starting from the square root.

        Intuition:
            The width closest to the square root of the area yields the
            smallest difference between length and width.

        Approach:
            Start from floor(sqrt(area)) and decrement until a divisor
            is found. Return [length, width] where length >= width.

        Complexity:
            Time: O(sqrt(area))
            Space: O(1)
        """
        width = int(sqrt(area))
        while area % width != 0:
            width -= 1
        return [area // width, width]
