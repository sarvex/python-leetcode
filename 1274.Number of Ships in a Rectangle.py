# """
# This is Sea's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Sea:
#    def hasShips(self, topRight: 'Point', bottomLeft: 'Point') -> bool:
#
# class Point:
# 	def __init__(self, x: int, y: int):
# 		self.x = x
# 		self.y = y


class Solution:
    def countShips(self, sea: "Sea", topRight: "Point", bottomLeft: "Point") -> int:
        """Count the number of ships in a rectangular region.

        Intuition:
            Divide the rectangle into four quadrants and recursively count
            ships in each. Use the hasShips API to prune empty regions.

        Approach:
            Recursively split the rectangle into four quadrants. For each
            quadrant, first check if any ships exist using the API. If not,
            skip it. Base case: a single point with ships returns 1.

        Complexity:
            Time: O(S * log(area)) where S is the number of ships
            Space: O(log(area)) recursion depth
        """

        def dfs(top_right: "Point", bottom_left: "Point") -> int:
            x1, y1 = bottom_left.x, bottom_left.y
            x2, y2 = top_right.x, top_right.y
            if x1 > x2 or y1 > y2:
                return 0
            if not sea.hasShips(top_right, bottom_left):
                return 0
            if x1 == x2 and y1 == y2:
                return 1
            mid_x = (x1 + x2) >> 1
            mid_y = (y1 + y2) >> 1
            top_right_quadrant = dfs(top_right, Point(mid_x + 1, mid_y + 1))
            top_left_quadrant = dfs(Point(mid_x, y2), Point(x1, mid_y + 1))
            bottom_left_quadrant = dfs(Point(mid_x, mid_y), bottom_left)
            bottom_right_quadrant = dfs(Point(x2, mid_y), Point(mid_x + 1, y1))
            return (
                top_right_quadrant
                + top_left_quadrant
                + bottom_left_quadrant
                + bottom_right_quadrant
            )

        return dfs(topRight, bottomLeft)
