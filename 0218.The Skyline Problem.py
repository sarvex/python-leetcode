from queue import PriorityQueue


class Solution:
    def getSkyline(self, buildings: list[list[int]]) -> list[list[int]]:
        """Priority queue sweep line to compute the skyline.

        Intuition:
            Process vertical sweep lines at each building edge. Use a max-heap
            to track the tallest active building at each position.

        Approach:
            1. Collect all x-coordinates (left and right edges) and sort them.
            2. For each sweep line, add buildings whose left edge <= current x.
            3. Remove expired buildings (right edge <= current x) from the heap.
            4. Record a skyline point when the max height changes.

        Complexity:
            Time: O(n^2) worst case due to priority queue operations per line
            Space: O(n) for the priority queue and result
        """
        skyline: list[list[int]] = []
        sweep_lines: list[int] = []
        priority_queue: PriorityQueue = PriorityQueue()
        for building in buildings:
            sweep_lines.extend([building[0], building[1]])
        sweep_lines.sort()
        building_idx, num_buildings = 0, len(buildings)
        for line in sweep_lines:
            while building_idx < num_buildings and buildings[building_idx][0] <= line:
                priority_queue.put(
                    [
                        -buildings[building_idx][2],
                        buildings[building_idx][0],
                        buildings[building_idx][1],
                    ]
                )
                building_idx += 1
            while not priority_queue.empty() and priority_queue.queue[0][2] <= line:
                priority_queue.get()
            height = 0
            if not priority_queue.empty():
                height = -priority_queue.queue[0][0]
            if len(skyline) > 0 and skyline[-1][1] == height:
                continue
            skyline.append([line, height])
        return skyline
