class Solution:
    def entityParser(self, text: str) -> str:
        """Replace HTML entities with their corresponding special characters.

        Intuition:
            Scan through the text and replace known HTML entity patterns
            with their decoded characters.

        Approach:
            Iterate character by character. At each position, try matching
            substrings of varying lengths against the entity dictionary.
            Replace matched entities with their decoded form.

        Complexity:
            Time: O(n) where n is the text length (constant entity lengths)
            Space: O(n) for the output buffer
        """
        entity_map = {
            "&quot;": '"',
            "&apos;": "'",
            "&amp;": "&",
            "&gt;": ">",
            "&lt;": "<",
            "&frasl;": "/",
        }
        position, length = 0, len(text)
        result: list[str] = []
        while position < length:
            for entity_length in range(1, 8):
                end = position + entity_length
                if text[position:end] in entity_map:
                    result.append(entity_map[text[position:end]])
                    position = end
                    break
            else:
                result.append(text[position])
                position += 1
        return "".join(result)
