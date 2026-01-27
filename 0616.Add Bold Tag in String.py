class Trie:
    def __init__(self) -> None:
        self.children: list[Trie | None] = [None] * 128
        self.is_end: bool = False

    def insert(self, word: str) -> None:
        node = self
        for char in word:
            idx = ord(char)
            if node.children[idx] is None:
                node.children[idx] = Trie()
            node = node.children[idx]
        node.is_end = True


class Solution:
    def addBoldTag(self, s: str, words: list[str]) -> str:
        """Add bold tags around substrings found in words using trie matching.

        Intuition:
            Use a trie to efficiently find all occurrences of dictionary words
            in the string, merge overlapping intervals, then wrap bold regions.

        Approach:
            1. Build a trie from the words list.
            2. For each position in s, find all word matches using the trie.
            3. Collect match intervals and merge overlapping ones.
            4. Build the result string, inserting <b> and </b> tags around
               merged intervals.

        Complexity:
            Time: O(n^2 + m) where n is string length and m is total word characters
            Space: O(m + n)
        """
        trie = Trie()
        for word in words:
            trie.insert(word)
        length = len(s)
        pairs: list[list[int]] = []
        for i in range(length):
            node = trie
            for j in range(i, length):
                idx = ord(s[j])
                if node.children[idx] is None:
                    break
                node = node.children[idx]
                if node.is_end:
                    pairs.append([i, j])
        if not pairs:
            return s
        start, end = pairs[0]
        merged: list[list[int]] = []
        for interval_start, interval_end in pairs[1:]:
            if end + 1 < interval_start:
                merged.append([start, end])
                start, end = interval_start, interval_end
            else:
                end = max(end, interval_end)
        merged.append([start, end])

        result: list[str] = []
        i = merge_idx = 0
        while i < length:
            if merge_idx == len(merged):
                result.append(s[i:])
                break
            start, end = merged[merge_idx]
            if i < start:
                result.append(s[i:start])
            result.append("<b>")
            result.append(s[start : end + 1])
            result.append("</b>")
            merge_idx += 1
            i = end + 1

        return "".join(result)
