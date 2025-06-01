from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val: int = 0, next: 'ListNode' = None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Add two numbers represented as linked lists where digits are stored in reverse order.

        Intuition:
        - Traverse both lists simultaneously, adding corresponding digits and keeping track of carry.
        - The result is built as a new linked list.

        Approach:
        1. Initialize a dummy node to serve as the head of the result list.
        2. Traverse both lists until we reach the end of both lists and there's no carry left.
        3. At each step, calculate the sum of current digits and carry.
        4. Create a new node with the units digit of the sum and update carry for the next iteration.
        5. Move to the next nodes in both lists if they exist.

        Complexity:
        Time: O(max(m, n)) where m and n are the lengths of l1 and l2.
        Space: O(max(m, n)) for the resulting linked list.
        """
        dummy = ListNode()  # Dummy node to simplify edge cases
        current = dummy
        carry = 0

        # Traverse both lists until we reach the end of both and there's no carry
        while l1 or l2 or carry:
            # Get values from current nodes or 0 if node is None
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            # Calculate sum and carry
            total = val1 + val2 + carry
            carry, digit = divmod(total, 10)

            # Create new node and move current pointer
            current.next = ListNode(digit)
            current = current.next

            # Move to next nodes if they exist
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next
