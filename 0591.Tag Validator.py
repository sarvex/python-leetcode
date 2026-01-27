class Solution:
    def isValid(self, code: str) -> bool:
        """Validate XML-like tag structure using a stack-based parser.

        Intuition:
            Parse the string character by character, tracking open tags on a
            stack. Handle CDATA sections, opening tags, and closing tags
            separately, ensuring proper nesting.

        Approach:
            1. Iterate through the code string.
            2. If we encounter CDATA, skip to the closing marker.
            3. For closing tags, pop from stack and verify tag name matches.
            4. For opening tags, validate tag name length and push onto stack.
            5. Return true only if the stack is empty after full traversal.

        Complexity:
            Time: O(n)
            Space: O(n)
        """

        def is_valid_tag(tag: str) -> bool:
            return 1 <= len(tag) <= 9 and all(char.isupper() for char in tag)

        stack: list[str] = []
        i, length = 0, len(code)
        while i < length:
            if i and not stack:
                return False
            if code[i : i + 9] == "<![CDATA[":
                i = code.find("]]>", i + 9)
                if i < 0:
                    return False
                i += 2
            elif code[i : i + 2] == "</":
                j = i + 2
                i = code.find(">", j)
                if i < 0:
                    return False
                tag = code[j:i]
                if not is_valid_tag(tag) or not stack or stack.pop() != tag:
                    return False
            elif code[i] == "<":
                j = i + 1
                i = code.find(">", j)
                if i < 0:
                    return False
                tag = code[j:i]
                if not is_valid_tag(tag):
                    return False
                stack.append(tag)
            i += 1
        return not stack
