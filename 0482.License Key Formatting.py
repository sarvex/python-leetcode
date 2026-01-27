class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        """Reformat license key with uppercase groups of size k.

        Intuition:
            The first group can be shorter than k; compute its size from
            the total alphanumeric character count modulo k.

        Approach:
            Count non-dash characters to determine the first group size.
            Iterate through the string, skipping dashes, uppercasing each
            character, and inserting dashes after every k characters.

        Complexity:
            Time: O(n)
            Space: O(n) for the result
        """
        length = len(s)
        first_group_size = (length - s.count("-")) % k or k
        result: list[str] = []
        for i, char in enumerate(s):
            if char == "-":
                continue
            result.append(char.upper())
            first_group_size -= 1
            if first_group_size == 0:
                first_group_size = k
                if i != length - 1:
                    result.append("-")
        return "".join(result).rstrip("-")
