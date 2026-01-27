class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        """Remove minimum parentheses to make string valid using two passes.

        Intuition:
            Invalid parentheses are unmatched closing ')' when no open '(' exists,
            and unmatched opening '(' when no closing ')' follows. Two passes can
            handle each direction independently.

        Approach:
            First pass left-to-right removes unmatched ')' by tracking open count.
            Second pass right-to-left removes unmatched '(' by tracking close count.
            Each pass skips characters that would create an imbalance.

        Complexity:
            Time: O(n) — two linear passes through the string
            Space: O(n) — for intermediate and result character lists
        """
        forward_pass: list[str] = []
        open_count = 0
        for char in s:
            if char == ")" and open_count == 0:
                continue
            if char == "(":
                open_count += 1
            elif char == ")":
                open_count -= 1
            forward_pass.append(char)

        close_count = 0
        backward_result: list[str] = []
        for char in reversed(forward_pass):
            if char == "(" and close_count == 0:
                continue
            if char == ")":
                close_count += 1
            elif char == "(":
                close_count -= 1
            backward_result.append(char)
        return "".join(reversed(backward_result))
