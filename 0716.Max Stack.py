from sortedcontainers import SortedList


class Node:
    def __init__(self, val: int = 0) -> None:
        self.val = val
        self.prev: Node | None = None
        self.next: Node | None = None


class DoubleLinkedList:
    def __init__(self) -> None:
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def append(self, val: int) -> Node:
        node = Node(val)
        node.next = self.tail
        node.prev = self.tail.prev
        self.tail.prev = node
        node.prev.next = node
        return node

    @staticmethod
    def remove(node: Node) -> Node:
        node.prev.next = node.next
        node.next.prev = node.prev
        return node

    def pop(self) -> Node:
        return self.remove(self.tail.prev)

    def peek(self) -> int:
        return self.tail.prev.val


class MaxStack:
    """Max stack using doubly linked list and sorted list.

    Intuition:
        A doubly linked list provides O(1) append/remove at any position,
        while a sorted list enables O(log n) access to the maximum element.

    Approach:
        1. Maintain a doubly linked list for stack order.
        2. Maintain a SortedList sorted by value for max access.
        3. push: append to list and add to sorted list.
        4. pop: remove from list tail and remove from sorted list.
        5. popMax: remove max from sorted list and remove its node from list.

    Complexity:
        Time: O(log n) for push, pop, popMax, peekMax; O(1) for top
        Space: O(n) for storing all elements
    """

    def __init__(self) -> None:
        self.stk = DoubleLinkedList()
        self.sl: SortedList = SortedList(key=lambda x: x.val)

    def push(self, x: int) -> None:
        node = self.stk.append(x)
        self.sl.add(node)

    def pop(self) -> int:
        node = self.stk.pop()
        self.sl.remove(node)
        return node.val

    def top(self) -> int:
        return self.stk.peek()

    def peekMax(self) -> int:
        return self.sl[-1].val

    def popMax(self) -> int:
        node = self.sl.pop()
        DoubleLinkedList.remove(node)
        return node.val
