from collections import deque
from threading import Semaphore


class BoundedBlockingQueue:
    """Thread-safe bounded blocking queue using semaphores.

    Intuition:
        Use two semaphores to block producers when full and consumers when
        empty, ensuring thread-safe bounded access.

    Approach:
        One semaphore tracks available capacity (initialized to capacity),
        the other tracks available items (initialized to 0). Enqueue acquires
        capacity and releases items; dequeue does the reverse.

    Complexity:
        Time: O(1) per operation (excluding blocking wait)
        Space: O(capacity)
    """

    def __init__(self, capacity: int) -> None:
        self.capacity_semaphore = Semaphore(capacity)
        self.item_semaphore = Semaphore(0)
        self.queue: deque[int] = deque()

    def enqueue(self, element: int) -> None:
        """Add an element, blocking if queue is full."""
        self.capacity_semaphore.acquire()
        self.queue.append(element)
        self.item_semaphore.release()

    def dequeue(self) -> int:
        """Remove and return an element, blocking if queue is empty."""
        self.item_semaphore.acquire()
        result = self.queue.popleft()
        self.capacity_semaphore.release()
        return result

    def size(self) -> int:
        """Return current number of elements in the queue."""
        return len(self.queue)
