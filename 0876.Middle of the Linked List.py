# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        """Slow and fast pointer technique to find the middle node.

        Intuition:
            Use two pointers moving at different speeds. When the fast
            pointer reaches the end, the slow pointer is at the middle.

        Approach:
            1. Initialize both slow and fast pointers at the head.
            2. Move slow by one step and fast by two steps each iteration.
            3. When fast reaches the end, return slow as the middle node.

        Complexity:
            Time: O(n)
            Space: O(1)
        """
        slow = fast = head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        return slow
