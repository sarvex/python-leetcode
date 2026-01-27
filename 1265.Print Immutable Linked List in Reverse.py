# """
# This is the ImmutableListNode's API interface.
# You should not implement it, or speculate about its implementation.
# """
# class ImmutableListNode:
#     def printValue(self) -> None: # print the value of this node.
#     def getNext(self) -> 'ImmutableListNode': # return the next node.


class Solution:
    def printLinkedListInReverse(self, head: "ImmutableListNode") -> None:
        """Print the values of an immutable linked list in reverse order.

        Intuition:
            Without the ability to modify the list, recursion naturally
            reverses the processing order by leveraging the call stack.

        Approach:
            Recursively traverse to the end of the list, then print each
            node's value as the call stack unwinds.

        Complexity:
            Time: O(n)
            Space: O(n) for the recursion stack
        """
        if head:
            self.printLinkedListInReverse(head.getNext())
            head.printValue()
