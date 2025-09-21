from collections import deque
from typing import Deque, Dict, List
import bisect

class Router:

    def __init__(self, memoryLimit: int):
        """Optimized packet router with O(1) add/forward and O(log n) range queries.

        Intuition:
            Maintain FIFO for forwarding, a set for duplicates, and per-destination
            time indexes to answer range count queries efficiently.

        Approach:
            - FIFO queue (deque) stores packets as (source, destination, timestamp).
            - A `seen` set prevents duplicates.
            - For each destination, keep a monotonically non-decreasing list of
              timestamps (`dest_times[dest]`) and a `head` pointer (`dest_head[dest]`)
              indicating how many earliest timestamps have been removed from storage.
              Adds append to the list; removals only advance the head.
            - Range counts use bisect on the suffix starting at `head`.

        Complexity:
            - addPacket: amortized O(1)
            - forwardPacket: O(1)
            - getCount: O(log k) where k is the number of stored packets for destination
        """
        self.limit: int = memoryLimit
        self.q: Deque[tuple[int, int, int]] = deque()
        self.seen: set[tuple[int, int, int]] = set()
        self.dest_times: Dict[int, List[int]] = {}
        self.dest_head: Dict[int, int] = {}

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        """Add a packet if not a duplicate; evict oldest if at capacity.

        Intuition:
            Use a set for duplicate detection and evict from FIFO when needed.

        Approach:
            - If packet exists in `seen`, return False.
            - If capacity reached, pop from FIFO, update `seen`, and advance the
              destination's head pointer.
            - Append new packet to FIFO, record in `seen`, and append timestamp
              to the destination's time list (initializing structures lazily).

        Complexity:
            Time O(1) amortized, Space O(n) up to memoryLimit across structures.
        """
        pkt = (source, destination, timestamp)
        if pkt in self.seen:
            return False

        if len(self.q) == self.limit:
            os, od, ot = self.q.popleft()
            self.seen.remove((os, od, ot))
            # Advance head for the evicted packet's destination.
            self.dest_head[od] = self.dest_head.get(od, 0) + 1

        # Record packet
        self.q.append(pkt)
        self.seen.add(pkt)

        times = self.dest_times.get(destination)
        if times is None:
            self.dest_times[destination] = [timestamp]
            # Initialize head if unseen destination
            if destination not in self.dest_head:
                self.dest_head[destination] = 0
        else:
            times.append(timestamp)

        return True

    def forwardPacket(self) -> List[int]:
        """Forward the next packet in FIFO order or return [].

        Intuition:
            FIFO pop with consistent per-destination head advancement.

        Approach:
            - Pop from queue, remove from `seen`, advance `dest_head[destination]`.
            - Return the packet triplet as a list.

        Complexity:
            Time O(1), Space O(1) auxiliary.
        """
        if not self.q:
            return []

        s, d, t = self.q.popleft()
        self.seen.remove((s, d, t))
        self.dest_head[d] = self.dest_head.get(d, 0) + 1
        return [s, d, t]

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        """Count stored packets with given destination and timestamp in [startTime, endTime].

        Intuition:
            Timestamps per destination are non-decreasing; use binary search on
            the active suffix starting at `head`.

        Approach:
            - If destination absent, return 0.
            - Use bisect_left/bisect_right with `lo=head` to bound the range.

        Complexity:
            Time O(log k) where k is active count for destination, Space O(1).
        """
        times = self.dest_times.get(destination)
        if not times:
            return 0

        head = self.dest_head.get(destination, 0)
        lo = bisect.bisect_left(times, startTime, lo=head)
        hi = bisect.bisect_right(times, endTime, lo=head)
        return hi - lo


# Your Router object will be instantiated and called as such:
# obj = Router(memoryLimit)
# param_1 = obj.addPacket(source,destination,timestamp)
# param_2 = obj.forwardPacket()
# param_3 = obj.getCount(destination,startTime,endTime)