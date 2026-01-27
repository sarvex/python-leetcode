class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        """Validate by checking IPv4 and IPv6 format rules.

        Intuition:
            An IP address is either IPv4 (4 decimal groups 0-255) or IPv6
            (8 hex groups of 1-4 characters). Check each format separately.

        Approach:
            Split by '.' for IPv4 and ':' for IPv6. Validate each group
            against the respective format constraints: no leading zeros for
            IPv4, valid hex characters for IPv6.

        Complexity:
            Time: O(n) where n is the length of the input string
            Space: O(n) for split results
        """

        def is_ipv4(address: str) -> bool:
            segments = address.split(".")
            if len(segments) != 4:
                return False
            for segment in segments:
                if len(segment) > 1 and segment[0] == "0":
                    return False
                if not segment.isdigit() or not 0 <= int(segment) <= 255:
                    return False
            return True

        def is_ipv6(address: str) -> bool:
            segments = address.split(":")
            if len(segments) != 8:
                return False
            for segment in segments:
                if not 1 <= len(segment) <= 4:
                    return False
                if not all(char in "0123456789abcdefABCDEF" for char in segment):
                    return False
            return True

        if is_ipv4(queryIP):
            return "IPv4"
        if is_ipv6(queryIP):
            return "IPv6"
        return "Neither"
