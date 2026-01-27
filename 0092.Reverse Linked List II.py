class ListNode:
    def __init__(self, val: int = 0, next: "ListNode | None" = None) -> None:
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(
        self, head: ListNode | None, left: int, right: int
    ) -> ListNode | None:
        """In-Place Sublist Reversal

        Intuition:
            Reverse only the portion of the linked list between positions
            left and right by re-linking the pointers in that segment.

        Approach:
            Use a dummy node for edge cases. Advance to the node just before
            position left. Reverse the sublist from left to right by iterating
            (right - left + 1) times and relinking pointers. Reconnect the
            reversed segment back into the original list.

        Complexity:
            Time: O(n)
            Space: O(1)
        """
        if head.next is None or left == right:
            return head
        dummy = ListNode(0, head)
        before_left = dummy
        for _ in range(left - 1):
            before_left = before_left.next
        sublist_start, sublist_end = before_left, before_left.next
        current = sublist_end
        for _ in range(right - left + 1):
            temp = current.next
            current.next = before_left
            before_left, current = current, temp
        sublist_start.next = before_left
        sublist_end.next = current
        return dummy.next
