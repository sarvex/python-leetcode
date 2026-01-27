class ListNode:
    def __init__(self, val: int = 0, next: "ListNode | None" = None) -> None:
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:
        """Single-Pass Duplicate Removal

        Intuition:
            Since the list is sorted, duplicates are adjacent. Simply skip
            the next node when its value matches the current node.

        Approach:
            Traverse the list. If the current node's value equals the next
            node's value, bypass the next node. Otherwise, advance to the
            next node.

        Complexity:
            Time: O(n)
            Space: O(1)
        """
        current = head
        while current and current.next:
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next
        return head
