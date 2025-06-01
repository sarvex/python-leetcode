from typing import List, Tuple


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        """Text Justification

        Intuition: Process words line by line, calculating spaces needed for justification.

        Approach:
        1. Process words sequentially, packing as many as possible into each line
        2. For each line except the last one:
           - Distribute spaces evenly between words
           - If spaces can't be distributed evenly, put extra spaces from left to right
        3. For the last line or lines with only one word:
           - Left-justify and fill remaining space with spaces

        Complexity:
        Time: O(n), where n is the total number of words
        Space: O(n), for storing the result lines
        """
        result = []
        i, n = 0, len(words)

        def pack_words() -> Tuple[List[str], int]:
            """Pack as many words as possible into a line and return the line and next word index."""
            nonlocal i
            line = [words[i]]
            length = len(words[i])
            i += 1

            while i < n and length + 1 + len(words[i]) <= maxWidth:
                line.append(words[i])
                length += 1 + len(words[i])  # +1 for the space
                i += 1

            return line, length

        def left_justify(line: List[str]) -> str:
            """Left justify a line of text and pad with spaces."""
            text = ' '.join(line)
            return text + ' ' * (maxWidth - len(text))

        def full_justify(line: List[str], word_length: int) -> str:
            """Fully justify text by distributing spaces between words."""
            if len(line) == 1:
                return line[0] + ' ' * (maxWidth - len(line[0]))

            total_spaces = maxWidth - word_length
            gaps = len(line) - 1
            spaces_per_gap, extra_spaces = divmod(total_spaces, gaps)

            justified = []
            for j, word in enumerate(line[:-1]):
                justified.append(word)
                space_count = spaces_per_gap + (1 if j < extra_spaces else 0)
                justified.append(' ' * space_count)

            justified.append(line[-1])
            return ''.join(justified)

        while i < n:
            current_line, _ = pack_words()
            word_length = sum(len(word) for word in current_line)

            # Handle last line or line with only one word (left-justified)
            if i == n or len(current_line) == 1:
                result.append(left_justify(current_line))
            else:
                result.append(full_justify(current_line, word_length))

        return result
