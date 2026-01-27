class Solution:
    def addTwoNumbers(
        self, list1: "ListNode | None", list2: "ListNode | None"
    ) -> "ListNode | None":
        """Stack-based addition of two linked lists in most-significant-digit-first order.

        Intuition:
            Since numbers are stored with the most significant digit first,
            use stacks to reverse the order and add from least significant digit.

        Approach:
            1. Push all values from both lists onto separate stacks.
            2. Pop from both stacks simultaneously, adding with carry.
            3. Build the result list by prepending each new node to the front.

        Complexity:
            Time: O(m + n) where m and n are the lengths of the two lists.
            Space: O(m + n) for the two stacks.
        """
        stack1: list[int] = []
        stack2: list[int] = []
        while list1:
            stack1.append(list1.val)
            list1 = list1.next
        while list2:
            stack2.append(list2.val)
            list2 = list2.next
        dummy = ListNode()
        carry = 0
        while stack1 or stack2 or carry:
            total = (
                (0 if not stack1 else stack1.pop())
                + (0 if not stack2 else stack2.pop())
                + carry
            )
            carry, digit = divmod(total, 10)
            dummy.next = ListNode(digit, dummy.next)
        return dummy.next
