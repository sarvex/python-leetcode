class ListNode:
    def __init__(self, val: int = 0, next: "ListNode | None" = None) -> None:
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:
        """Two-Pointer Duplicate Removal

        Intuition:
            In a sorted list, duplicates are adjacent. Use a predecessor
            pointer to skip over all nodes with duplicated values.

        Approach:
            Create a dummy node before head. Track a predecessor pointer.
            For each current node, advance through consecutive duplicates.
            If predecessor.next still points to current (no duplicates found),
            advance predecessor. Otherwise, link predecessor.next past all
            the duplicates.

        Complexity:
            Time: O(n)
            Space: O(1)
        """
        dummy = predecessor = ListNode(next=head)
        current = head
        while current:
            while current.next and current.next.val == current.val:
                current = current.next
            if predecessor.next == current:
                predecessor = current
            else:
                predecessor.next = current.next
            current = current.next
        return dummy.next
