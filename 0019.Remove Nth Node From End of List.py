from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        Two-pointer technique to remove the nth node from the end of a linked list.

        Intuition:
        Use a fast and slow pointer with a gap of n nodes between them. When the fast
        pointer reaches the end, the slow pointer will be at the node just before the
        one we want to remove.

        Approach:
        1. Create a dummy node to handle edge cases (like removing the head).
        2. Initialize fast and slow pointers at the dummy node.
        3. Advance fast pointer n steps ahead.
        4. Move both pointers until fast reaches the end.
        5. Remove the nth node by updating the next pointer of slow.
        6. Return the head of the modified list (dummy.next).

        Complexity:
        Time: O(L) where L is the length of the linked list, as we traverse the list once.
        Space: O(1) as we only use two pointers regardless of list size.
        """
        # Create a dummy node to handle edge cases like removing the head
        dummy = ListNode(next=head)
        fast = slow = dummy

        # Advance fast pointer n steps ahead
        for _ in range(n):
            fast = fast.next

        # Move both pointers until fast reaches the end
        while fast.next:
            slow, fast = slow.next, fast.next

        # Remove the nth node by updating the next pointer
        slow.next = slow.next.next

        # Return the head of the modified list
        return dummy.next
