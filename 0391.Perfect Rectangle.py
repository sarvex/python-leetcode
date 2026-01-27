from collections import defaultdict


class Solution:
    def isRectangleCover(self, rectangles: list[list[int]]) -> bool:
        """Verify perfect rectangle cover using area and corner counting.

        Intuition:
            A perfect rectangle cover requires two conditions: the total area
            of all rectangles equals the bounding rectangle area, and every
            corner appears an even number of times except the four corners
            of the bounding rectangle which appear exactly once.

        Approach:
            1. Compute total area and bounding box coordinates.
            2. Count corner occurrences for all rectangles.
            3. Verify total area matches bounding rectangle area.
            4. Verify the four bounding corners each appear exactly once.
            5. Verify all other corners appear exactly 2 or 4 times.

        Complexity:
            Time: O(n) where n is the number of rectangles
            Space: O(n) for the corner count map
        """
        total_area = 0
        min_x, min_y = rectangles[0][0], rectangles[0][1]
        max_x, max_y = rectangles[0][2], rectangles[0][3]
        corner_count: dict[tuple[int, int], int] = defaultdict(int)

        for rect in rectangles:
            total_area += (rect[2] - rect[0]) * (rect[3] - rect[1])

            min_x = min(min_x, rect[0])
            min_y = min(min_y, rect[1])
            max_x = max(max_x, rect[2])
            max_y = max(max_y, rect[3])

            corner_count[(rect[0], rect[1])] += 1
            corner_count[(rect[0], rect[3])] += 1
            corner_count[(rect[2], rect[3])] += 1
            corner_count[(rect[2], rect[1])] += 1

        if (
            total_area != (max_x - min_x) * (max_y - min_y)
            or corner_count[(min_x, min_y)] != 1
            or corner_count[(min_x, max_y)] != 1
            or corner_count[(max_x, max_y)] != 1
            or corner_count[(max_x, min_y)] != 1
        ):
            return False

        del (
            corner_count[(min_x, min_y)],
            corner_count[(min_x, max_y)],
            corner_count[(max_x, max_y)],
            corner_count[(max_x, min_y)],
        )

        return all(count == 2 or count == 4 for count in corner_count.values())
