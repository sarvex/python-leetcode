class Solution:
    def lengthLongestPath(self, input: str) -> int:
        """Stack-based simulation of directory traversal.

        Intuition:
            The tab count indicates the depth level. We can use a stack
            to track cumulative path lengths at each depth, popping when
            we return to a shallower level.

        Approach:
            1. Iterate character by character through the input.
            2. Count leading tabs to determine indentation level.
            3. Measure the current name length and check for file extension.
            4. Pop the stack until its size matches the indentation level.
            5. Accumulate path length (add 1 for separator if stack non-empty).
            6. For directories, push onto stack; for files, update max length.

        Complexity:
            Time: O(n) where n is the length of the input string
            Space: O(d) where d is the maximum depth of nesting
        """
        index, length = 0, len(input)
        max_length = 0
        path_stack: list[int] = []
        while index < length:
            indent = 0
            while input[index] == "\t":
                indent += 1
                index += 1

            current_length, is_file = 0, False
            while index < length and input[index] != "\n":
                current_length += 1
                if input[index] == ".":
                    is_file = True
                index += 1
            index += 1

            while len(path_stack) > 0 and len(path_stack) > indent:
                path_stack.pop()

            if len(path_stack) > 0:
                current_length += path_stack[-1] + 1

            if not is_file:
                path_stack.append(current_length)
                continue

            max_length = max(max_length, current_length)

        return max_length
