class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        """Two Pointer Convergence.

        Intuition:
            If two pointers traverse both lists by switching to the other list's
            head upon reaching the end, they will meet at the intersection node
            or both reach None simultaneously.

        Approach:
            Initialize two pointers at the heads of the two lists. Advance each
            pointer one step at a time. When a pointer reaches the end, redirect
            it to the head of the other list. The pointers will converge at the
            intersection node after at most two passes.

        Complexity:
            Time: O(m + n) where m and n are the lengths of the two lists
            Space: O(1) only two pointers used
        """
        pointer_a, pointer_b = headA, headB
        while pointer_a != pointer_b:
            pointer_a = pointer_a.next if pointer_a else headB
            pointer_b = pointer_b.next if pointer_b else headA
        return pointer_a
