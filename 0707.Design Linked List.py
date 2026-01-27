class MyLinkedList:
    """Singly linked list with dummy head for uniform insertion/deletion.

    Intuition:
        A dummy head node simplifies edge cases for operations at the head.
        Maintaining a count allows O(1) bounds checking for index validity.

    Approach:
        1. Use a dummy head node so insertions and deletions at any index
           follow the same pattern.
        2. Track the count of elements for bounds checking.
        3. For get/add/delete, traverse to the target position from the dummy.

    Complexity:
        Time: O(n) for get, addAtIndex, deleteAtIndex; O(1) for addAtHead
        Space: O(n) for storing n elements
    """

    def __init__(self) -> None:
        self.dummy = ListNode()
        self.count = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.count:
            return -1
        current = self.dummy.next
        for _ in range(index):
            current = current.next
        return current.val

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.count, val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.count:
            return
        predecessor = self.dummy
        for _ in range(index):
            predecessor = predecessor.next
        predecessor.next = ListNode(val, predecessor.next)
        self.count += 1

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.count:
            return
        predecessor = self.dummy
        for _ in range(index):
            predecessor = predecessor.next
        target = predecessor.next
        predecessor.next = target.next
        target.next = None
        self.count -= 1
