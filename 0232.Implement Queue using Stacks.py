class MyQueue:
    """Queue implementation using two stacks.

    Intuition:
        Two stacks can simulate a queue by reversing element order. Pushing
        onto one stack and popping from the reversed stack gives FIFO behavior.

    Approach:
        Use an input stack for pushes and an output stack for pops. When the
        output stack is empty, lazily transfer all elements from the input
        stack, reversing their order. This achieves amortized O(1) per
        operation since each element is moved at most twice.

    Complexity:
        Time: O(1) amortized per operation
        Space: O(n) for storing all elements across two stacks
    """

    def __init__(self) -> None:
        """Initialize input and output stacks."""
        self.input_stack: list[int] = []
        self.output_stack: list[int] = []

    def push(self, x: int) -> None:
        """Push element to the back of the queue."""
        self.input_stack.append(x)

    def pop(self) -> int:
        """Remove and return the front element."""
        self._transfer()
        return self.output_stack.pop()

    def peek(self) -> int:
        """Return the front element without removing it."""
        self._transfer()
        return self.output_stack[-1]

    def empty(self) -> bool:
        """Return whether the queue is empty."""
        return not self.input_stack and not self.output_stack

    def _transfer(self) -> None:
        """Move elements from input to output stack if output is empty."""
        if not self.output_stack:
            while self.input_stack:
                self.output_stack.append(self.input_stack.pop())
