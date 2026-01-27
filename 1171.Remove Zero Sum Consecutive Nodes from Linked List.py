class ListNode:
    def __init__(self, val: int = 0, next: "ListNode | None" = None):
        self.val = val
        self.next = next


class Solution:
    def removeZeroSumSublists(self, head: ListNode | None) -> ListNode | None:
        """Remove zero-sum consecutive nodes from linked list.

        Intuition:
            If two prefix sums are equal, the nodes between them sum to zero and
            can be removed.

        Approach:
            Use a dummy head and compute prefix sums while recording the last node
            for each prefix sum value. Then iterate again, linking each node directly
            to the node after the last occurrence of its prefix sum.

        Complexity:
            Time: O(n)
            Space: O(n)
        """
        dummy = ListNode(next=head)
        last_seen: dict[int, ListNode] = {}
        prefix_sum = 0
        current = dummy
        while current:
            prefix_sum += current.val
            last_seen[prefix_sum] = current
            current = current.next

        prefix_sum = 0
        current = dummy
        while current:
            prefix_sum += current.val
            current.next = last_seen[prefix_sum].next
            current = current.next

        return dummy.next
