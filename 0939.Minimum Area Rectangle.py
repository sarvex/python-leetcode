import math
from collections import defaultdict


class Solution:
    def minAreaRect(self, points: list[list[int]]) -> int:
        """Sweep line by x-coordinate tracking y-pairs for rectangle detection.

        Intuition:
            For each pair of y-values sharing the same x-coordinate, check if
            we previously saw the same y-pair at a smaller x, forming a rectangle.

        Approach:
            1. Group points by x-coordinate.
            2. Process x-values in sorted order.
            3. For each pair of y-values at current x, check if the pair was seen before.
            4. If so, compute rectangle area using current x minus previous x.
            5. Track the minimum area found.

        Complexity:
            Time: O(n^2) — worst case iterating y-pairs per x
            Space: O(n^2) — storing y-pair to x mappings
        """
        columns = defaultdict(list)
        for x_coord, y_coord in points:
            columns[x_coord].append(y_coord)
        last_x_for_pair = {}
        min_area = math.inf
        for x_coord in sorted(columns):
            y_values = columns[x_coord]
            y_values.sort()
            num_y = len(y_values)
            for i, y_lower in enumerate(y_values):
                for y_upper in y_values[i + 1 :]:
                    if (y_lower, y_upper) in last_x_for_pair:
                        min_area = min(
                            min_area,
                            (x_coord - last_x_for_pair[(y_lower, y_upper)])
                            * (y_upper - y_lower),
                        )
                    last_x_for_pair[(y_lower, y_upper)] = x_coord
        return 0 if min_area == math.inf else min_area
