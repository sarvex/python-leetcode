from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """Iterative approach with constant space complexity

        Intuition:
        Use a dummy node to build the reversed list. For each node in the original list,
        insert it at the beginning of the new list, effectively reversing the order.

        Approach:
        1. Create a dummy node to serve as the head of the reversed list
        2. Iterate through the original list
        3. For each node, detach it from the original list and insert it at the beginning of the new list
        4. Return the head of the reversed list (dummy.next)

        Complexity:
        Time: O(n) where n is the number of nodes in the linked list
        Space: O(1) as we only use a constant amount of extra space
        """
        previous = None
        current = head

        while current:
            next_node = current.next  # Store the next node
            current.next = previous       # Reverse the link
            previous = current            # Move prev one step forward
            current = next_node       # Move current one step forward

        return previous
