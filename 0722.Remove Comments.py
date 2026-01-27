class Solution:
    def removeComments(self, source: list[str]) -> list[str]:
        """State machine to strip line and block comments from source code.

        Intuition:
            Process characters one by one, toggling between normal mode and
            block comment mode, skipping everything inside comments.

        Approach:
            1. Iterate through each line character by character.
            2. In normal mode, detect '//' (skip rest of line) or '/*' (enter
               block comment mode).
            3. In block comment mode, detect '*/' to exit.
            4. Collect non-comment characters and emit non-empty lines.

        Complexity:
            Time: O(n) where n is total characters across all lines
            Space: O(n) for the output
        """
        result: list[str] = []
        current_line: list[str] = []
        in_block_comment = False
        for line in source:
            idx, length = 0, len(line)
            while idx < length:
                if in_block_comment:
                    if idx + 1 < length and line[idx : idx + 2] == "*/":
                        in_block_comment = False
                        idx += 1
                else:
                    if idx + 1 < length and line[idx : idx + 2] == "/*":
                        in_block_comment = True
                        idx += 1
                    elif idx + 1 < length and line[idx : idx + 2] == "//":
                        break
                    else:
                        current_line.append(line[idx])
                idx += 1
            if not in_block_comment and current_line:
                result.append("".join(current_line))
                current_line.clear()
        return result
