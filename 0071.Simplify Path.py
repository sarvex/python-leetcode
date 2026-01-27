class Solution:
    def simplifyPath(self, path: str) -> str:
        """Stack-Based Path Simplification

        Intuition:
            Split the path by '/' and process each component. A stack
            naturally handles '..' by popping the last directory.

        Approach:
            Split the path on '/'. Skip empty segments and '.'. For '..',
            pop from the stack if non-empty. Otherwise, push the directory
            name onto the stack. Join the result with '/' and prepend '/'.

        Complexity:
            Time: O(n) where n is the length of the path
            Space: O(n)
        """
        stack: list[str] = []
        for segment in path.split("/"):
            if not segment or segment == ".":
                continue
            if segment == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(segment)
        return "/" + "/".join(stack)
