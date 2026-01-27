class Solution:
    def reorderList(self, head: ListNode | None) -> None:
        """Split, reverse second half, then interleave two halves.

        Intuition:
            Reordering alternates between front and back of the list. Splitting
            at the midpoint, reversing the back half, and merging the two halves
            achieves this in-place.

        Approach:
            1. Use slow/fast pointers to find the middle of the list.
            2. Split the list into two halves at the middle.
            3. Reverse the second half in-place.
            4. Interleave nodes from the first and reversed second halves.

        Complexity:
            Time: O(n)
            Space: O(1)
        """
        fast = slow = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        current = slow.next
        slow.next = None

        previous = None
        while current:
            next_node = current.next
            current.next = previous
            previous, current = current, next_node
        current = head

        while previous:
            next_node = previous.next
            previous.next = current.next
            current.next = previous
            current, previous = previous.next, next_node
