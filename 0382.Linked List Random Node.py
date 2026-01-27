import random


class ListNode:
    def __init__(self, val: int = 0, next: "ListNode | None" = None) -> None:
        self.val = val
        self.next = next


class Solution:
    """Reservoir sampling for random node selection from a linked list."""

    def __init__(self, head: ListNode | None) -> None:
        """Initialize with the head of the linked list."""
        self.head = head

    def getRandom(self) -> int:
        """Return a random node's value with equal probability using reservoir sampling.

        Intuition:
            Reservoir sampling allows uniform random selection from a stream
            of unknown length in a single pass.

        Approach:
            Traverse the list, keeping a count of nodes seen. For the nth node,
            replace the current answer with probability 1/n. This guarantees
            each node has equal probability of being selected.

        Complexity:
            Time: O(n)
            Space: O(1)
        """
        count = 0
        result = 0
        current = self.head
        while current:
            count += 1
            if random.randint(1, count) == count:
                result = current.val
            current = current.next
        return result
