from collections import deque


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        """BFS Shortest Path Approach

        Intuition:
            Each word transformation changes exactly one character. This forms a
            graph where BFS finds the shortest path from beginWord to endWord.

        Approach:
            Add all words to a set for O(1) lookup. Use BFS starting from beginWord,
            trying all 26 character substitutions at each position. Track visited
            words by removing them from the set. Return the transformation count
            when endWord is reached.

        Complexity:
            Time: O(n * m * 26) where n is word count and m is word length
            Space: O(n * m) for the word set and queue
        """
        words = set(wordList)
        queue = deque([beginWord])
        steps = 1
        while queue:
            steps += 1
            for _ in range(len(queue)):
                current = queue.popleft()
                chars = list(current)
                for i in range(len(chars)):
                    original_char = chars[i]
                    for j in range(26):
                        chars[i] = chr(ord("a") + j)
                        transformed = "".join(chars)
                        if transformed not in words:
                            continue
                        if transformed == endWord:
                            return steps
                        queue.append(transformed)
                        words.remove(transformed)
                    chars[i] = original_char
        return 0
