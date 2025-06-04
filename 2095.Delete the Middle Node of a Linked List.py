from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """Fast and slow pointer technique to find and delete the middle node.

        Intuition:
        Use the classic tortoise and hare algorithm (slow and fast pointers) to find the middle node.
        The slow pointer moves one step at a time while the fast pointer moves two steps.
        When the fast pointer reaches the end, the slow pointer will be just before the middle node.

        Approach:
        1. Handle edge cases: if head is None or there's only one node, return None
        2. Use a dummy node pointing to head to handle edge cases cleanly
        3. Initialize slow pointer at dummy and fast pointer at head
        4. Move slow one step at a time and fast two steps at a time
        5. When fast reaches the end, slow will be just before the middle node
        6. Delete the middle node by updating the next pointer of slow
        7. Return the dummy's next (which is the head of the modified list)

        Complexity:
        Time: O(n) where n is the number of nodes in the linked list
        Space: O(1) as we only use constant extra space regardless of input size
        """
        if not head or not head.next:
            return None

        dummy = ListNode(next=head)
        slow, fast = dummy, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        slow.next = slow.next.next

        return dummy.next
