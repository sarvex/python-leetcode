class ListNode:
    def __init__(self, val: int = 0, next: "ListNode | None" = None) -> None:
        self.val = val
        self.next = next


class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        """Add one to a number represented as a linked list using rightmost non-nine tracking.

        Intuition:
            Adding one only affects trailing 9s and the rightmost non-9 digit.
            All trailing 9s become 0, and the rightmost non-9 increments by 1.

        Approach:
            Use a dummy node in case of full carry (e.g., 999 -> 1000). Traverse
            the list tracking the rightmost node that is not 9. After traversal,
            increment that node and set all subsequent nodes to 0. Return the
            dummy node if it was incremented, otherwise return the original head.

        Complexity:
            Time: O(n)
            Space: O(1)
        """
        dummy = ListNode(0, head)
        rightmost_non_nine = dummy
        while head:
            if head.val != 9:
                rightmost_non_nine = head
            head = head.next
        rightmost_non_nine.val += 1
        rightmost_non_nine = rightmost_non_nine.next
        while rightmost_non_nine:
            rightmost_non_nine.val = 0
            rightmost_non_nine = rightmost_non_nine.next
        return dummy if dummy.val else dummy.next
