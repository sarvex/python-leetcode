from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Two-pointer approach: Separate odd and even nodes into two lists and connect them.

        Intuition:
        We can traverse the linked list and separate nodes into odd and even positions.
        Then connect the last odd node to the first even node.

        Approach:
        1. Use two pointers: odd_ptr for odd positions and even_ptr for even positions
        2. Keep track of even_head to connect after processing
        3. Iterate through the list, connecting odd nodes together and even nodes together
        4. Finally, connect the end of odd list to the start of even list

        Complexity:
        Time: O(n) where n is the number of nodes in the linked list
        Space: O(1) as we only use constant extra space
        """
        if head is None:
            return None

        odd = head
        middle = even = head.next

        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next

        odd.next = middle

        return head
