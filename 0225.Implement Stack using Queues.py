from collections import deque


class MyStack:
    """Stack implementation using two queues.

    Intuition:
        A queue is FIFO while a stack is LIFO. By reversing the order of
        elements after each push, the front of the queue always holds the
        most recently pushed element.

    Approach:
        On push, add the new element to the secondary queue, then drain all
        elements from the primary queue into the secondary queue. Swap the
        two queues so that primary always has stack order. Pop and top
        simply operate on the front of the primary queue.

    Complexity:
        Time: O(n) per push, O(1) per pop, top, and empty
        Space: O(n) for storing all elements across two queues
    """

    def __init__(self) -> None:
        """Initialize two internal queues."""
        self.primary: deque[int] = deque()
        self.secondary: deque[int] = deque()

    def push(self, x: int) -> None:
        """Push element onto the stack."""
        self.secondary.append(x)
        while self.primary:
            self.secondary.append(self.primary.popleft())
        self.primary, self.secondary = self.secondary, self.primary

    def pop(self) -> int:
        """Remove and return the top element."""
        return self.primary.popleft()

    def top(self) -> int:
        """Return the top element without removing it."""
        return self.primary[0]

    def empty(self) -> bool:
        """Return whether the stack is empty."""
        return len(self.primary) == 0
