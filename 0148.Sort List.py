class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        """Merge Sort on Linked List.

        Intuition:
            Use merge sort to achieve O(n log n) sorting on a linked list
            by recursively splitting and merging halves.

        Approach:
            Find the middle of the list using slow/fast pointers, split into
            two halves, recursively sort each half, then merge the two sorted
            halves back together.

        Complexity:
            Time: O(n log n) for merge sort
            Space: O(log n) for recursion stack depth
        """
        if head is None or head.next is None:
            return head
        slow, fast = head, head.next
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        second_half = slow.next
        slow.next = None
        left, right = self.sortList(head), self.sortList(second_half)
        dummy = ListNode()
        current = dummy
        while left and right:
            if left.val <= right.val:
                current.next = left
                left = left.next
            else:
                current.next = right
                right = right.next
            current = current.next
        current.next = left or right
        return dummy.next
