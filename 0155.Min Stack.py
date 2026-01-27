from math import inf


class MinStack:
    """Stack supporting push, pop, top, and O(1) minimum retrieval.

    Intuition:
        Maintain a parallel stack that tracks the minimum value at each level
        so that getMin is always O(1).

    Approach:
        Use two stacks: one for actual values and one for tracking the running
        minimum. On push, append the value and also append the min of the
        current value and the top of the min stack. On pop, pop from both.

    Complexity:
        Time: O(1) for all operations
        Space: O(n) for the two stacks
    """

    def __init__(self) -> None:
        """Initialize the MinStack with an empty value stack and a min stack seeded with infinity."""
        self.stk1: list[int] = []
        self.stk2: list[float] = [inf]

    def push(self, val: int) -> None:
        """Push value onto the stack and update minimum tracker."""
        self.stk1.append(val)
        self.stk2.append(min(val, self.stk2[-1]))

    def pop(self) -> None:
        """Remove the top element from the stack."""
        self.stk1.pop()
        self.stk2.pop()

    def top(self) -> int:
        """Return the top element of the stack."""
        return self.stk1[-1]

    def getMin(self) -> int:
        """Return the minimum element in the stack."""
        return self.stk2[-1]
