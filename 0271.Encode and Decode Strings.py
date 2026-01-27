class Codec:
    """Encode and decode a list of strings using length-prefixed format.

    Intuition:
        By prefixing each string with its length, we can unambiguously
        reconstruct the original list without worrying about delimiters
        appearing within the strings themselves.

    Approach:
        Encode each string by prepending a fixed-width 4-digit length prefix,
        then concatenate all prefixed strings. To decode, repeatedly read the
        4-character length prefix, extract the corresponding substring, and
        advance the read position.

    Complexity:
        Time: O(n) for both encode and decode where n is total character count
        Space: O(n) for the encoded/decoded output
    """

    def encode(self, strs: list[str]) -> str:
        """Encode a list of strings to a single string."""
        parts: list[str] = []
        for string in strs:
            parts.append(f"{len(string):4}{string}")
        return "".join(parts)

    def decode(self, s: str) -> list[str]:
        """Decode a single string back to a list of strings."""
        result: list[str] = []
        index, length = 0, len(s)
        while index < length:
            size = int(s[index : index + 4])
            index += 4
            result.append(s[index : index + size])
            index += size
        return result
