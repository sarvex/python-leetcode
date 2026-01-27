class Trie:
    def __init__(self) -> None:
        self.children: list[Trie | None] = [None] * 128
        self.is_end: bool = False

    def insert(self, word: str) -> None:
        node = self
        for ch in word:
            idx = ord(ch)
            if node.children[idx] is None:
                node.children[idx] = Trie()
            node = node.children[idx]
        node.is_end = True


class Solution:
    def boldWords(self, words: list[str], s: str) -> str:
        """Trie-based matching with interval merging to wrap bold substrings.

        Intuition:
            Use a trie to find all substrings in s that match any word,
            merge overlapping intervals, and wrap them in <b> tags.

        Approach:
            1. Insert all words into a trie.
            2. For each starting index, walk the trie to find all matching
               end positions, collecting [start, end] pairs.
            3. Merge overlapping/adjacent intervals.
            4. Build the result string with bold tags around merged intervals.

        Complexity:
            Time: O(N^2 + W*L) where N = len(s), W = words count, L = word length
            Space: O(W*L + N)
        """
        trie = Trie()
        for word in words:
            trie.insert(word)
        length = len(s)
        match_pairs: list[list[int]] = []
        for i in range(length):
            node = trie
            for j in range(i, length):
                idx = ord(s[j])
                if node.children[idx] is None:
                    break
                node = node.children[idx]
                if node.is_end:
                    match_pairs.append([i, j])
        if not match_pairs:
            return s
        merged_start, merged_end = match_pairs[0]
        merged: list[list[int]] = []
        for start, end in match_pairs[1:]:
            if merged_end + 1 < start:
                merged.append([merged_start, merged_end])
                merged_start, merged_end = start, end
            else:
                merged_end = max(merged_end, end)
        merged.append([merged_start, merged_end])

        result: list[str] = []
        pos = interval_idx = 0
        while pos < length:
            if interval_idx == len(merged):
                result.append(s[pos:])
                break
            seg_start, seg_end = merged[interval_idx]
            if pos < seg_start:
                result.append(s[pos:seg_start])
            result.append("<b>")
            result.append(s[seg_start : seg_end + 1])
            result.append("</b>")
            interval_idx += 1
            pos = seg_end + 1

        return "".join(result)
