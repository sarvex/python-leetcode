from itertools import product


class Solution:
    def assignBikes(
        self, workers: list[list[int]], bikes: list[list[int]]
    ) -> list[int]:
        """Assign bikes to workers by shortest Manhattan distance greedily.

        Intuition:
            Sort all worker-bike pairs by distance, then greedily assign
            unmatched pairs.

        Approach:
            Compute all pairwise Manhattan distances, sort by (distance, worker,
            bike), then assign first available bike to each unassigned worker.

        Complexity:
            Time: O(n * m * log(n * m)) for sorting all pairs
            Space: O(n * m) for the pairs array
        """
        worker_count, bike_count = len(workers), len(bikes)
        pairs = []
        for i, j in product(range(worker_count), range(bike_count)):
            distance = abs(workers[i][0] - bikes[j][0]) + abs(
                workers[i][1] - bikes[j][1]
            )
            pairs.append((distance, i, j))
        pairs.sort()
        worker_assigned = [False] * worker_count
        bike_assigned = [False] * bike_count
        assignment = [0] * worker_count
        for _, worker_idx, bike_idx in pairs:
            if not worker_assigned[worker_idx] and not bike_assigned[bike_idx]:
                worker_assigned[worker_idx] = bike_assigned[bike_idx] = True
                assignment[worker_idx] = bike_idx
        return assignment
