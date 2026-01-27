class Solution:
    def distanceBetweenBusStops(
        self, distance: list[int], start: int, destination: int
    ) -> int:
        """Find minimum distance between two bus stops on a circular route.

        Intuition:
            A circular bus route has two paths between any two stops. The shorter
            path is the minimum of clockwise and counter-clockwise distances.

        Approach:
            Traverse clockwise from start to destination summing distances. The
            counter-clockwise distance is total route distance minus the clockwise
            distance. Return the minimum.

        Complexity:
            Time: O(n)
            Space: O(1)
        """
        clockwise_distance = 0
        stop_count = len(distance)
        current = start
        while current != destination:
            clockwise_distance += distance[current]
            current = (current + 1) % stop_count
        return min(clockwise_distance, sum(distance) - clockwise_distance)
