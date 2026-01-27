class Solution:
    def restoreIpAddresses(self, s: str) -> list[str]:
        """Backtracking Approach

        Intuition:
            An IP address has exactly 4 octets, each between 0 and 255 with
            no leading zeros. Try all valid placements of the 3 dots.

        Approach:
            Use DFS to build octets. At each step, try substrings of length
            1 to 3 starting from the current index. Validate each substring
            (no leading zeros, value <= 255). When 4 valid octets are formed
            and the entire string is consumed, record the result.

        Complexity:
            Time: O(1) — bounded by at most 3^4 combinations
            Space: O(1) — bounded output size
        """

        def is_valid_octet(start: int, end: int) -> bool:
            if s[start] == "0" and start != end:
                return False
            return 0 <= int(s[start : end + 1]) <= 255

        def dfs(start: int) -> None:
            if start >= length and len(octets) == 4:
                result.append(".".join(octets))
                return
            if start >= length or len(octets) >= 4:
                return
            for end in range(start, min(start + 3, length)):
                if is_valid_octet(start, end):
                    octets.append(s[start : end + 1])
                    dfs(end + 1)
                    octets.pop()

        length = len(s)
        result: list[str] = []
        octets: list[str] = []
        dfs(0)
        return result
