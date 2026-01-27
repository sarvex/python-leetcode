class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        """Insertion Sort on Linked List.

        Intuition:
            Simulate insertion sort by maintaining a sorted portion and
            inserting each subsequent node into its correct position.

        Approach:
            Use a dummy node as the sorted list head. Traverse the original
            list, and for each node find the correct insertion point in the
            sorted portion by scanning from the dummy head.

        Complexity:
            Time: O(n^2) in the worst case for insertion sort
            Space: O(1) as sorting is done in-place on the linked list
        """
        if head is None or head.next is None:
            return head
        dummy = ListNode(head.val, head)
        prev, current = dummy, head
        while current:
            if prev.val <= current.val:
                prev, current = current, current.next
                continue
            insert_pos = dummy
            while insert_pos.next.val <= current.val:
                insert_pos = insert_pos.next
            next_node = current.next
            current.next = insert_pos.next
            insert_pos.next = current
            prev.next = next_node
            current = next_node
        return dummy.next
