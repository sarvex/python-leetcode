class Solution:
    def isValid(self, s: str) -> bool:
        """Stack-based validation of parentheses matching

        Intuition:
        Use a stack to keep track of opening brackets and match them with closing brackets.
        When we encounter a closing bracket, it should match the most recent opening bracket.

        Approach:
        1. Iterate through each character in the string
        2. If it's an opening bracket, push it onto the stack
        3. If it's a closing bracket, check if it matches the top of the stack
        4. If the stack is empty at the end, all brackets were properly matched

        Complexity:
        Time: O(n) where n is the length of the string
        Space: O(n) in the worst case when all characters are opening brackets
        """
        stack = []
        pairs = {'(': ')', '[': ']', '{': '}'}

        for char in s:
            if char in pairs:  # Opening bracket
                stack.append(char)
            else:  # Closing bracket
                if not stack or pairs[stack.pop()] != char:
                    return False

        return len(stack) == 0
