from sortedcontainers import SortedSet


class DinnerPlates:
    """Dinner plate stacks with fixed capacity per stack.

    Intuition:
        We need efficient access to the leftmost non-full stack for push and the
        rightmost non-empty stack for pop, plus arbitrary stack access for popAtStack.

    Approach:
        Maintain a list of stacks and a sorted set tracking indices of non-full stacks.
        Push goes to the leftmost non-full stack. Pop removes from the rightmost
        non-empty stack, cleaning up trailing empty stacks. popAtStack handles
        arbitrary index access.

    Complexity:
        Time: O(log n) per push/pop/popAtStack operation
        Space: O(n) for all elements stored
    """

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.stacks: list[list[int]] = []
        self.not_full = SortedSet()

    def push(self, val: int) -> None:
        if not self.not_full:
            self.stacks.append([val])
            if self.capacity > 1:
                self.not_full.add(len(self.stacks) - 1)
        else:
            index = self.not_full[0]
            self.stacks[index].append(val)
            if len(self.stacks[index]) == self.capacity:
                self.not_full.discard(index)

    def pop(self) -> int:
        return self.popAtStack(len(self.stacks) - 1)

    def popAtStack(self, index: int) -> int:
        if index < 0 or index >= len(self.stacks) or not self.stacks[index]:
            return -1
        val = self.stacks[index].pop()
        if index == len(self.stacks) - 1 and not self.stacks[-1]:
            while self.stacks and not self.stacks[-1]:
                self.not_full.discard(len(self.stacks) - 1)
                self.stacks.pop()
        else:
            self.not_full.add(index)
        return val
