from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        """Two-pointer approach with fast and slow pointers

        Intuition: The twin sum can be found by pairing nodes from the first half with reversed
        nodes from the second half. We can use fast and slow pointers to find the middle,
        then reverse the second half in-place to calculate the maximum twin sum.

        Approach:
        1. Use fast and slow pointers to find the middle of the linked list
        2. Reverse the second half of the linked list in-place
        3. Iterate through both halves simultaneously to find the maximum twin sum

        Complexity:
        Time: O(n) where n is the number of nodes in the linked list
        Space: O(1) as we only use a constant amount of extra space
        """
        # Find the middle of the linked list using fast and slow pointers
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse the second half of the linked list
        previous, current = None, slow
        while current:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node

        # Calculate the maximum twin sum
        first, second = head, previous
        max_sum = 0
        while second:
            max_sum = max(max_sum, first.val + second.val)
            first = first.next
            second = second.next

        return max_sum
