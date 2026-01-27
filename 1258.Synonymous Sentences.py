from collections import defaultdict
from itertools import chain


class UnionFind:
    def __init__(self, n: int) -> None:
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a: int, b: int) -> None:
        root_a, root_b = self.find(a), self.find(b)
        if root_a != root_b:
            if self.size[root_a] > self.size[root_b]:
                self.parent[root_b] = root_a
                self.size[root_a] += self.size[root_b]
            else:
                self.parent[root_a] = root_b
                self.size[root_b] += self.size[root_a]


class Solution:
    def generateSentences(self, synonyms: list[list[str]], text: str) -> list[str]:
        """Generate all sentences by replacing words with their synonyms.

        Intuition:
            Synonyms form equivalence classes. Union-Find groups all synonymous
            words together. We then generate all combinations by replacing each
            word with every synonym in its group.

        Approach:
            Collect unique words from synonym pairs. Use Union-Find to group
            synonyms. For each word in the sentence, if it has synonyms,
            branch into all sorted alternatives via DFS backtracking.

        Complexity:
            Time: O(S * P^W) where S is sentence length, P is max synonym group size, W is replaceable words
            Space: O(n + output size)
        """

        def dfs(index: int) -> None:
            if index >= len(words):
                result.append(" ".join(current))
                return
            if words[index] not in word_to_id:
                current.append(words[index])
                dfs(index + 1)
                current.pop()
            else:
                root = uf.find(word_to_id[words[index]])
                for member_id in groups[root]:
                    current.append(all_words[member_id])
                    dfs(index + 1)
                    current.pop()

        all_words = list(set(chain.from_iterable(synonyms)))
        word_to_id = {w: i for i, w in enumerate(all_words)}
        uf = UnionFind(len(word_to_id))
        for word_a, word_b in synonyms:
            uf.union(word_to_id[word_a], word_to_id[word_b])
        groups: dict[int, list[int]] = defaultdict(list)
        for i in range(len(all_words)):
            groups[uf.find(i)].append(i)
        for key in groups:
            groups[key].sort(key=lambda i: all_words[i])
        words = text.split()
        result: list[str] = []
        current: list[str] = []
        dfs(0)
        return result
