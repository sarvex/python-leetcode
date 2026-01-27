from heapq import heappush, heappop


class Solution:
    def scheduleCourse(self, courses: list[list[int]]) -> int:
        """Greedy with max-heap to maximize number of courses taken.

        Intuition:
        Sort courses by deadline and greedily take each course. If adding a course
        exceeds its deadline, remove the longest-duration course taken so far.

        Approach:
        1. Sort courses by their last day (deadline).
        2. Use a max-heap (negative durations) to track taken courses.
        3. For each course, add it to the heap and accumulate time.
        4. If total time exceeds the deadline, pop the longest course to free time.
        5. The heap size at the end is the maximum number of courses.

        Complexity:
        Time: O(n log n)
        Space: O(n)
        """
        courses.sort(key=lambda x: x[1])
        max_heap = []
        total_time = 0
        for duration, last_day in courses:
            heappush(max_heap, -duration)
            total_time += duration
            while total_time > last_day:
                total_time += heappop(max_heap)
        return len(max_heap)
