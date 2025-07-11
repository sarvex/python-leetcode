from heapq import heapify, heappop, heappush
from typing import List


class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        """Two-heap approach for optimal room allocation and tracking.

        Intuition:
        We need to track which rooms are available and which are busy, while
        counting how many meetings each room hosts. The room with the most
        meetings should be returned, with ties broken by smallest room number.

        Approach:
        1. Sort meetings by start time to process chronologically
        2. Use two heaps: idle rooms (min-heap by room number) and busy rooms
           (min-heap by end time, then room number)
        3. For each meeting, free up rooms that have finished
        4. Assign to available room or delay meeting to earliest available room
        5. Track meeting count per room and return the most used room

        Complexity:
        Time: O(m log n) where m is meetings count, n is rooms count
        Space: O(n) for heaps and counters
        """
        meetings.sort()

        # Min-heap of available rooms by room number
        idle_rooms = list(range(n))
        heapify(idle_rooms)

        # Min-heap of busy rooms by (end_time, room_number)
        busy_rooms = []

        # Count meetings per room
        meeting_counts = [0] * n

        for start_time, end_time in meetings:
            self._free_finished_rooms(busy_rooms, idle_rooms, start_time)

            if idle_rooms:
                self._assign_to_idle_room(
                    idle_rooms, busy_rooms, meeting_counts,
                    start_time, end_time
                )
            else:
                self._delay_meeting_to_next_available(
                    busy_rooms, meeting_counts, start_time, end_time
                )

        return self._find_most_used_room(meeting_counts)

    def _free_finished_rooms(
        self,
        busy_rooms: List[tuple],
        idle_rooms: List[int],
        current_time: int
    ) -> None:
        """Move rooms from busy to idle if their meetings have ended."""
        while busy_rooms and busy_rooms[0][0] <= current_time:
            _, room_number = heappop(busy_rooms)
            heappush(idle_rooms, room_number)

    def _assign_to_idle_room(
        self,
        idle_rooms: List[int],
        busy_rooms: List[tuple],
        meeting_counts: List[int],
        start_time: int,
        end_time: int
    ) -> None:
        """Assign meeting to the lowest numbered available room."""
        room_number = heappop(idle_rooms)
        meeting_counts[room_number] += 1
        heappush(busy_rooms, (end_time, room_number))

    def _delay_meeting_to_next_available(
        self,
        busy_rooms: List[tuple],
        meeting_counts: List[int],
        start_time: int,
        end_time: int
    ) -> None:
        """Delay meeting to the earliest available room."""
        earliest_end_time, room_number = heappop(busy_rooms)
        meeting_counts[room_number] += 1

        # Meeting duration remains the same, but starts when room is free
        meeting_duration = end_time - start_time
        new_end_time = earliest_end_time + meeting_duration

        heappush(busy_rooms, (new_end_time, room_number))

    def _find_most_used_room(self, meeting_counts: List[int]) -> int:
        """Find room with most meetings, breaking ties by smallest room number."""
        most_used_room = 0
        for room_number, count in enumerate(meeting_counts):
            if count > meeting_counts[most_used_room]:
                most_used_room = room_number
        return most_used_room
