class Solution:
    def busyStudent(
        self, startTime: list[int], endTime: list[int], queryTime: int
    ) -> int:
        """Count students doing homework at queryTime.

        Intuition:
            A student is busy if queryTime falls within their start and end times.

        Approach:
            Zip start and end times together and count how many intervals
            contain the query time.

        Complexity:
            Time: O(n)
            Space: O(1)
        """
        return sum(start <= queryTime <= end for start, end in zip(startTime, endTime))
