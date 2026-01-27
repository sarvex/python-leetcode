class ListNode:
    def __init__(self, x: int):
        self.val = x
        self.next: ListNode | None = None


class Solution:
    def detectCycle(self, head: ListNode | None) -> ListNode | None:
        """Floyd's Tortoise and Hare Algorithm

        Intuition:
            Using two pointers at different speeds, if a cycle exists they will
            meet inside the cycle. The distance from head to cycle start equals
            the distance from the meeting point to cycle start.

        Approach:
            Use slow and fast pointers. When they meet, move one pointer back to
            head and advance both one step at a time. They will meet at the cycle
            start node.

        Complexity:
            Time: O(n) where n is the number of nodes
            Space: O(1)
        """
        fast = slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                entry = head
                while entry != slow:
                    entry = entry.next
                    slow = slow.next
                return entry
        return None
