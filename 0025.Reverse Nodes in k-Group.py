# Definition for singly-linked list.
class ListNode:
    def __init__(self, val: int = 0, next: 'ListNode' = None) -> None:
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: ListNode | None, k: int) -> ListNode | None:
        """Reverse nodes in k-group

        Intuition:
        - We need to reverse every k nodes in the linked list
        - For each group, we need to:
          1. Check if there are at least k nodes left
          2. Reverse those k nodes
          3. Connect the reversed group back to the list

        Approach:
        - Use a dummy node to handle edge cases
        - Traverse the list, counting k nodes at a time
        - For each group of k nodes:
          - Check if we have k nodes (if not, leave them as is)
          - Reverse the k nodes using a helper function
          - Connect the reversed group back to the list
        - Use pointers to keep track of the previous group's end and current position

        Complexity:
        - Time: O(n), where n is the number of nodes in the list
        - Space: O(1), only using constant extra space for pointers
        """
        if not head or k <= 1:
            return head

        def reverse_sublist(head: ListNode) -> ListNode:
            """Reverse a linked list and return the new head"""
            prev, curr = None, head
            while curr:
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node
            return prev

        dummy = ListNode(0, head)
        prev = curr = dummy

        while curr.next:
            # Try to move k steps forward
            for _ in range(k):
                curr = curr.next
                # Not enough nodes left
                if not curr:
                    return dummy.next

            # Save the next group's start
            next_group_start = curr.next

            # Disconnect the current group
            curr.next = None

            # Save the current group's start
            group_start = prev.next

            # Reverse the current group and connect it
            prev.next = reverse_sublist(group_start)

            # Connect the end of reversed group to the next group
            group_start.next = next_group_start

            # Update pointers for the next iteration
            prev = group_start
            curr = prev

        return dummy.next
