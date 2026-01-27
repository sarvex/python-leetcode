class Solution:
    def minAvailableDuration(
        self, slots1: list[list[int]], slots2: list[list[int]], duration: int
    ) -> list[int]:
        """Find the earliest common time slot of given duration.

        Intuition:
            Sorting both slot lists and using two pointers lets us efficiently
            find the first overlapping interval that is long enough.

        Approach:
            Sort both slot arrays. Use two pointers to find the overlap between
            current slots. If the overlap is at least duration, return the
            result. Otherwise advance the pointer with the earlier ending slot.

        Complexity:
            Time: O(m log m + n log n)
            Space: O(1)
        """
        slots1.sort()
        slots2.sort()
        total1, total2 = len(slots1), len(slots2)
        i = j = 0
        while i < total1 and j < total2:
            start = max(slots1[i][0], slots2[j][0])
            end = min(slots1[i][1], slots2[j][1])
            if end - start >= duration:
                return [start, start + duration]
            if slots1[i][1] < slots2[j][1]:
                i += 1
            else:
                j += 1
        return []
