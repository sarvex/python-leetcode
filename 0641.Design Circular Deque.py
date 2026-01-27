class MyCircularDeque:
    """Array-based circular deque with fixed capacity.

    Intuition:
    Use a fixed-size array with a front pointer and size counter to implement
    circular indexing for both front and rear operations.

    Approach:
    1. Maintain an array of size k, a front pointer, and current size.
    2. For insertFront, move front backward (circular) and place the value.
    3. For insertLast, compute rear index from front + size and place the value.
    4. For deletions, adjust front or size accordingly.

    Complexity:
    Time: O(1) for all operations
    Space: O(k)
    """

    def __init__(self, k: int) -> None:
        self.buffer = [0] * k
        self.front = 0
        self.size = 0
        self.capacity = k

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        if not self.isEmpty():
            self.front = (self.front - 1 + self.capacity) % self.capacity
        self.buffer[self.front] = value
        self.size += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        idx = (self.front + self.size) % self.capacity
        self.buffer[idx] = value
        self.size += 1
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        self.size -= 1
        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.buffer[self.front]

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        idx = (self.front + self.size - 1) % self.capacity
        return self.buffer[idx]

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.capacity
