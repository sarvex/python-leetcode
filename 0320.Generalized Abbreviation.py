class Solution:
    def generateAbbreviations(self, word: str) -> list[str]:
        """Recursive DFS generating all possible abbreviations.

        Intuition:
            At each position, either keep the character or start abbreviating
            a sequence of consecutive characters with their count.

        Approach:
            1. From position i, generate abbreviations by either keeping word[i]
               followed by all abbreviations of the rest, or abbreviating a
               substring starting at i of length 1..n-i.
            2. For abbreviated substrings, include the count, the next kept
               character (if any), and all abbreviations of what follows.

        Complexity:
            Time: O(n * 2^n) where n is the length of word
            Space: O(n * 2^n) for storing all abbreviations
        """

        def dfs(index: int) -> list[str]:
            if index >= length:
                return [""]
            abbreviations = [word[index] + suffix for suffix in dfs(index + 1)]
            for end in range(index + 1, length + 1):
                for suffix in dfs(end + 1):
                    abbreviations.append(
                        str(end - index) + (word[end] if end < length else "") + suffix
                    )
            return abbreviations

        length = len(word)
        return dfs(0)
