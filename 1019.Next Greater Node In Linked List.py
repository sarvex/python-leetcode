# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: ListNode | None) -> list[int]:
        """Next Greater Node In Linked List using monotonic stack.

        Intuition:
            Convert the linked list to an array, then use a decreasing
            monotonic stack traversed from right to left to find the next
            greater element for each node.

        Approach:
            First collect all values into a list. Then iterate from right to
            left, maintaining a stack of values in decreasing order. For each
            element, pop smaller or equal values, and the stack top (if any)
            is the next greater node.

        Complexity:
            Time: O(n)
            Space: O(n)
        """
        values: list[int] = []
        current = head
        while current:
            values.append(current.val)
            current = current.next

        stack: list[int] = []
        length = len(values)
        result = [0] * length
        for i in range(length - 1, -1, -1):
            while stack and stack[-1] <= values[i]:
                stack.pop()
            if stack:
                result[i] = stack[-1]
            stack.append(values[i])
        return result
