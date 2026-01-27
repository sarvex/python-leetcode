class Solution:
    def removeElements(self, head: ListNode | None, val: int) -> ListNode | None:
        """Remove all nodes with the target value using a dummy head.

        Intuition:
            A dummy node before the head simplifies edge cases where the head
            itself needs removal. Traverse with a pointer checking the next
            node's value.

        Approach:
            1. Create a dummy node pointing to head.
            2. Iterate: if the next node's value matches, skip it; otherwise
               advance the pointer.
            3. Return dummy.next as the new head.

        Complexity:
            Time: O(n)
            Space: O(1)
        """
        dummy = ListNode(-1, head)
        previous = dummy
        while previous.next:
            if previous.next.val != val:
                previous = previous.next
            else:
                previous.next = previous.next.next
        return dummy.next
