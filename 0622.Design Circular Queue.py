class MyCircularQueue:
    """Circular queue implementation using a fixed-size array with front pointer and size tracking.

    Intuition:
        Use a fixed array with modular arithmetic to wrap around, tracking
        the front index and current size to efficiently manage enqueue and
        dequeue operations.

    Approach:
        1. Maintain an array of size k, a front pointer, and a size counter.
        2. Enqueue inserts at (front + size) % capacity and increments size.
        3. Dequeue advances front by one modulo capacity and decrements size.
        4. Front and Rear are computed from front pointer and current size.

    Complexity:
        Time: O(1) for all operations
        Space: O(k)
    """

    def __init__(self, k: int) -> None:
        self.queue = [0] * k
        self.front = 0
        self.size = 0
        self.capacity = k

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        idx = (self.front + self.size) % self.capacity
        self.queue[idx] = value
        self.size += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return True

    def Front(self) -> int:
        return -1 if self.isEmpty() else self.queue[self.front]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        idx = (self.front + self.size - 1) % self.capacity
        return self.queue[idx]

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.capacity
