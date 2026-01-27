class Solution:
    def findLongestWord(self, s: str, dictionary: list[str]) -> str:
        """Check each dictionary word as a subsequence of s.

        Intuition:
            A word from the dictionary can be formed by deleting characters
            from s if it is a subsequence of s. Find the longest such word.

        Approach:
            For each word in the dictionary, check if it is a subsequence of s.
            Track the longest match, preferring lexicographically smaller on ties.

        Complexity:
            Time: O(d * n) where d is dictionary size, n = len(s)
            Space: O(1)
        """

        def is_subsequence(word: str, target: str) -> bool:
            word_idx = target_idx = 0
            while word_idx < len(word) and target_idx < len(target):
                if word[word_idx] == target[target_idx]:
                    word_idx += 1
                target_idx += 1
            return word_idx == len(word)

        result = ""
        for word in dictionary:
            if is_subsequence(word, s) and (
                len(result) < len(word) or (len(result) == len(word) and result > word)
            ):
                result = word
        return result
