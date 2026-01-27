class Solution:
    def intervalIntersection(
        self, first_list: list[list[int]], second_list: list[list[int]]
    ) -> list[list[int]]:
        """Find intersections of two sorted interval lists.

        Intuition:
            Two intervals intersect when the start of one is before the end of the
            other. We advance the pointer whose interval ends first.

        Approach:
            Use two pointers to walk through both lists. For each pair compute the
            overlap as [max(start), min(end)]. If valid, add to result. Advance the
            pointer with the smaller end value.

        Complexity:
            Time: O(m + n) where m and n are the lengths of the two lists
            Space: O(m + n) for the result in the worst case
        """
        i = j = 0
        result: list[list[int]] = []
        while i < len(first_list) and j < len(second_list):
            start1, end1, start2, end2 = *first_list[i], *second_list[j]
            low, high = max(start1, start2), min(end1, end2)
            if low <= high:
                result.append([low, high])
            if end1 < end2:
                i += 1
            else:
                j += 1
        return result
