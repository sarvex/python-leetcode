class Solution:
    def expressiveWords(self, s: str, words: list[str]) -> int:
        """Two-pointer group comparison for stretchy word matching.

        Intuition:
            A word is stretchy if each character group in the word matches the
            corresponding group in s, with s's group being >= 3 or exactly equal.

        Approach:
            1. For each word, compare character groups using two pointers.
            2. Groups must have the same character. The source group count must
               be >= the word group count, and if < 3, must be exactly equal.
            3. Count words that match.

        Complexity:
            Time: O(n * m) where n = len(words), m = max word length
            Space: O(1)
        """

        def is_stretchy(source: str, target: str) -> bool:
            source_len, target_len = len(source), len(target)
            if target_len > source_len:
                return False
            src_idx = tgt_idx = 0
            while src_idx < source_len and tgt_idx < target_len:
                if source[src_idx] != target[tgt_idx]:
                    return False
                src_end = src_idx
                while src_end < source_len and source[src_end] == source[src_idx]:
                    src_end += 1
                src_count = src_end - src_idx
                src_idx, tgt_end = src_end, tgt_idx
                while tgt_end < target_len and target[tgt_end] == target[tgt_idx]:
                    tgt_end += 1
                tgt_count = tgt_end - tgt_idx
                tgt_idx = tgt_end
                if src_count < tgt_count or (src_count < 3 and src_count != tgt_count):
                    return False
            return src_idx == source_len and tgt_idx == target_len

        return sum(is_stretchy(s, word) for word in words)
