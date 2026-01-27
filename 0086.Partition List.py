class ListNode:
    def __init__(self, val: int = 0, next: "ListNode | None" = None) -> None:
        self.val = val
        self.next = next


class Solution:
    def partition(self, head: ListNode | None, x: int) -> ListNode | None:
        """Two-Pointer Partition with Dummy Nodes

        Intuition:
            Separate nodes into two lists: one with values less than x
            and one with values greater than or equal to x, then concatenate.

        Approach:
            Create two dummy heads for the "less" and "greater-or-equal" lists.
            Traverse the original list, appending each node to the appropriate
            list. Finally, connect the tail of the "less" list to the head of
            the "greater-or-equal" list and terminate.

        Complexity:
            Time: O(n)
            Space: O(1)
        """
        less_dummy, greater_dummy = ListNode(), ListNode()
        less_tail, greater_tail = less_dummy, greater_dummy
        while head:
            if head.val < x:
                less_tail.next = head
                less_tail = less_tail.next
            else:
                greater_tail.next = head
                greater_tail = greater_tail.next
            head = head.next
        less_tail.next = greater_dummy.next
        greater_tail.next = None
        return less_dummy.next
