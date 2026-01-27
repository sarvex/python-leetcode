class Solution:
    def isPalindrome(self, head: ListNode | None) -> bool:
        """Fast-slow pointer with in-place reversal of the second half.

        Intuition:
            Find the middle of the list, reverse the second half, then compare
            both halves node by node.

        Approach:
            1. Use slow/fast pointers to find the midpoint.
            2. Reverse the linked list from the midpoint onward.
            3. Compare values from the head and the reversed second half.

        Complexity:
            Time: O(n)
            Space: O(1)
        """
        slow, fast = head, head.next
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        previous, current = None, slow.next
        while current:
            next_node = current.next
            current.next = previous
            previous, current = current, next_node
        while previous:
            if previous.val != head.val:
                return False
            previous, head = previous.next, head.next
        return True
