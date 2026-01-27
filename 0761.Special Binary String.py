class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        """Recursive decomposition to produce the lexicographically largest special string.

        Intuition:
            A special binary string can be split into independent special
            substrings. Recursively process each inner substring and sort
            the pieces in descending order.

        Approach:
            1. Scan for balanced segments (count of 1s equals count of 0s).
            2. Strip the outer '1' and '0', recurse on the inner part.
            3. Sort all segments in reverse order and concatenate.

        Complexity:
            Time: O(N^2) in the worst case
            Space: O(N) for recursion
        """
        if s == "":
            return ""
        segments: list[str] = []
        balance = 0
        start = 0
        for i in range(len(s)):
            balance += 1 if s[i] == "1" else -1
            if balance == 0:
                segments.append("1" + self.makeLargestSpecial(s[start + 1 : i]) + "0")
                start = i + 1
        segments.sort(reverse=True)
        return "".join(segments)
