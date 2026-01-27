class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        """Sort cars by position and count distinct arrival time groups.

        Intuition:
            Cars closer to the target that arrive later will block faster cars
            behind them, forming fleets. Sorting by position and scanning from
            closest to farthest lets us count fleet formations.

        Approach:
            1. Sort car indices by position
            2. Iterate from the car closest to target backwards
            3. Compute each car's arrival time
            4. If a car's time exceeds the previous fleet's time, it starts a new fleet

        Complexity:
            Time: O(n log n) for sorting
            Space: O(n) for the sorted index array
        """
        sorted_indices = sorted(range(len(position)), key=lambda i: position[i])
        fleet_count = 0
        previous_time = 0.0
        for idx in reversed(sorted_indices):
            arrival_time = (target - position[idx]) / speed[idx]
            if arrival_time > previous_time:
                fleet_count += 1
                previous_time = arrival_time
        return fleet_count
