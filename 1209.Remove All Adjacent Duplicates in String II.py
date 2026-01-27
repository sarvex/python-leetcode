class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        """Remove all adjacent duplicates in string II.

        Intuition:
            Track consecutive character runs using a stack of (char, count) pairs.
            When merging with the stack top, reduce counts modulo k to remove groups.

        Approach:
            Iterate through the string grouping consecutive identical characters.
            For each group, compute count modulo k. If the stack top has the same
            character, merge counts (again mod k). Pop if count reaches zero.

        Complexity:
            Time: O(n) where n is the length of the string
            Space: O(n) for the stack in the worst case
        """
        stack: list[list[str | int]] = []
        index, length = 0, len(s)
        while index < length:
            end = index
            while end < length and s[end] == s[index]:
                end += 1
            count = (end - index) % k
            if stack and stack[-1][0] == s[index]:
                stack[-1][1] = (stack[-1][1] + count) % k
                if stack[-1][1] == 0:
                    stack.pop()
            elif count:
                stack.append([s[index], count])
            index = end
        return "".join(char * count for char, count in stack)
