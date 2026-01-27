from itertools import pairwise


class Solution:
    def minmaxGasDist(self, stations: list[int], k: int) -> float:
        """Binary search on the maximum distance between adjacent stations.

        Intuition:
            The answer is monotonic: if we can achieve max distance d with k
            stations, we can also achieve any distance > d. This makes binary
            search applicable on the answer value.

        Approach:
            1. Binary search on the maximum allowed distance in [0, 1e8]
            2. For each candidate distance, check if the total stations needed
               (splitting each gap) is within budget k
            3. Narrow the search window until precision reaches 1e-6

        Complexity:
            Time: O(n * log(max_gap / epsilon)) where n is station count
            Space: O(1)
        """

        def is_feasible(max_distance: float) -> bool:
            return (
                sum(
                    int((right - left) / max_distance)
                    for left, right in pairwise(stations)
                )
                <= k
            )

        left, right = 0.0, 1e8
        while right - left > 1e-6:
            mid = (left + right) / 2
            if is_feasible(mid):
                right = mid
            else:
                left = mid
        return left
