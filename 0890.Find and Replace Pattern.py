class Solution:
    def findAndReplacePattern(self, words: list[str], pattern: str) -> list[str]:
        """Bijective character mapping check for pattern matching.

        Intuition:
            Two strings match the same pattern if there is a bijection between
            their characters. Track mappings in both directions simultaneously.

        Approach:
            1. For each word, check if a consistent bijection exists between
               word characters and pattern characters.
            2. Use two mapping arrays indexed by character ordinal, recording
               the position (1-indexed) of first association.
            3. If mappings conflict, the word does not match.

        Complexity:
            Time: O(n * m) where n is number of words, m is word length.
            Space: O(1) — mapping arrays have fixed size 128.
        """

        def matches(source: str, target: str) -> bool:
            source_map = [0] * 128
            target_map = [0] * 128
            for position, (source_char, target_char) in enumerate(
                zip(source, target), 1
            ):
                if source_map[ord(source_char)] != target_map[ord(target_char)]:
                    return False
                source_map[ord(source_char)] = target_map[ord(target_char)] = position
            return True

        return [word for word in words if matches(word, pattern)]
