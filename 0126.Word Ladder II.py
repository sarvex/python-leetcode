from collections import defaultdict, deque


class Solution:
    def findLadders(
        self, beginWord: str, endWord: str, wordList: list[str]
    ) -> list[list[str]]:
        """BFS Shortest Path with DFS Backtracking Approach

        Intuition:
            First find the shortest transformation distance using BFS, recording
            predecessors at each level. Then reconstruct all shortest paths by
            DFS backtracking from endWord to beginWord using the predecessor map.

        Approach:
            Build a word set and use BFS to explore one-character mutations level
            by level, tracking distance and predecessors. Once the endWord is found,
            use DFS to backtrack through predecessors and collect all shortest paths.

        Complexity:
            Time: O(n * m * 26) where n is word count and m is word length
            Space: O(n * m) for the predecessor map and queue
        """

        def dfs(path: list[str], current: str) -> None:
            if current == beginWord:
                result.append(path[::-1])
                return
            for precursor in predecessors[current]:
                path.append(precursor)
                dfs(path, precursor)
                path.pop()

        result: list[list[str]] = []
        words = set(wordList)
        if endWord not in words:
            return result
        words.discard(beginWord)
        distance = {beginWord: 0}
        predecessors: dict[str, set[str]] = defaultdict(set)
        queue = deque([beginWord])
        found = False
        step = 0
        while queue and not found:
            step += 1
            for _ in range(len(queue), 0, -1):
                current_word = queue.popleft()
                chars = list(current_word)
                for i in range(len(chars)):
                    original_char = chars[i]
                    for j in range(26):
                        chars[i] = chr(ord("a") + j)
                        transformed = "".join(chars)
                        if distance.get(transformed, 0) == step:
                            predecessors[transformed].add(current_word)
                        if transformed not in words:
                            continue
                        predecessors[transformed].add(current_word)
                        words.discard(transformed)
                        queue.append(transformed)
                        distance[transformed] = step
                        if endWord == transformed:
                            found = True
                    chars[i] = original_char
        if found:
            path = [endWord]
            dfs(path, endWord)
        return result
