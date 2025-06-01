from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """Rotate linked list to the right by k places

        Intuition: Find the length of the list, then calculate the effective rotation amount.
        Use two pointers to find the new head and tail positions after rotation.

        Approach:
        1. Handle edge cases: empty list, single node, or k = 0 after modulo
        2. Calculate the length of the linked list
        3. Adjust k to handle cases where k > length of list
        4. Use fast and slow pointers with k-gap to find the new break point
        5. Rearrange the pointers to create the rotated list

        Complexity:
        Time: O(n) where n is the length of the linked list
        Space: O(1) as we only use a constant amount of extra space
        """
        # Handle edge cases
        if not head or not head.next or k == 0:
            return head

        # Calculate the length of the list
        current, length = head, 0
        while current:
            length += 1
            current = current.next

        # Calculate effective rotation
        k %= length
        if k == 0:
            return head

        # Find the new head position using two pointers
        fast = slow = head
        for _ in range(k):
            fast = fast.next

        # Move both pointers until fast reaches the end
        while fast.next:
            fast = fast.next
            slow = slow.next

        # Rearrange the list
        new_head = slow.next
        slow.next = None
        fast.next = head

        return new_head
