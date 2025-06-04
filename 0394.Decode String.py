class Solution:
    def decodeString(self, s: str) -> str:
        """Stack-based nested string decoding

        Intuition:
        When we encounter digits, we're building a number. When we see '[', we need to
        remember both the number and the current result before starting a new nested string.
        When we see ']', we need to decode the nested string by repeating it.

        Approach:
        1. Use two stacks: one for numbers and one for partial results
        2. Parse the string character by character:
           - For digits: build the current number
           - For '[': push current number and result to respective stacks, reset both
           - For ']': pop number and previous result, then repeat current result and append
           - For letters: append to current result
        3. Return the final decoded string

        Complexity:
        Time: O(n), where n is the length of the input string
        Space: O(n), for the stacks in worst case of deeply nested strings
        """
        num_stack, str_stack = [], []
        current_num, current_str = 0, ''

        for char in s:
            if char.isdigit():
                current_num = current_num * 10 + int(char)
            elif char == '[':
                num_stack.append(current_num)
                str_stack.append(current_str)
                current_num, current_str = 0, ''
            elif char == ']':
                prev_str = str_stack.pop()
                repeat_count = num_stack.pop()
                current_str = prev_str + current_str * repeat_count
            else:
                current_str += char

        return current_str
