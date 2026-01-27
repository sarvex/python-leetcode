from heapq import heappop, heappush


class Solution:
    def minRefuelStops(
        self, target: int, start_fuel: int, stations: list[list[int]]
    ) -> int:
        """Greedy with max-heap to always refuel at the best past station.

        Intuition:
            Travel as far as possible and when fuel runs out, retroactively
            refuel at the station with the most fuel among those already passed.

        Approach:
            1. Append the target as a final station with zero fuel.
            2. For each station, subtract the distance traveled from fuel.
            3. While fuel is negative, pop the largest available fuel from the
               max-heap (stored as negatives) and increment the refuel count.
            4. If fuel is still negative after exhausting the heap, return -1.

        Complexity:
            Time: O(n log n)
            Space: O(n)
        """
        heap: list[int] = []
        previous_position = 0
        refuel_count = 0
        stations.append([target, 0])
        for position, fuel_amount in stations:
            distance = position - previous_position
            start_fuel -= distance
            while start_fuel < 0 and heap:
                start_fuel -= heappop(heap)
                refuel_count += 1
            if start_fuel < 0:
                return -1
            heappush(heap, -fuel_amount)
            previous_position = position
        return refuel_count
