class CustomStack:
    """Stack with fixed max size supporting push, pop, and lazy increment.

    Intuition:
        Use a lazy propagation technique for the increment operation. Instead
        of updating all bottom-k elements, store the increment at position k-1
        and propagate it downward only during pop.

    Approach:
        Maintain two arrays: one for stack values and one for accumulated
        increments. On increment(k, val), add val to the k-1 index of the
        increment array. On pop, add the stored increment to the result and
        propagate it to the element below.

    Complexity:
        Time: O(1) per push, pop, and increment operation.
        Space: O(max_size)
    """

    def __init__(self, max_size: int) -> None:
        self.stack = [0] * max_size
        self.increments = [0] * max_size
        self.top = 0

    def push(self, x: int) -> None:
        if self.top < len(self.stack):
            self.stack[self.top] = x
            self.top += 1

    def pop(self) -> int:
        if self.top <= 0:
            return -1
        self.top -= 1
        result = self.stack[self.top] + self.increments[self.top]
        if self.top > 0:
            self.increments[self.top - 1] += self.increments[self.top]
        self.increments[self.top] = 0
        return result

    def increment(self, k: int, val: int) -> None:
        index = min(k, self.top) - 1
        if index >= 0:
            self.increments[index] += val
