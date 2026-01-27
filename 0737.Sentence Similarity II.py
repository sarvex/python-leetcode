class Solution:
    def areSentencesSimilarTwo(
        self, sentence1: list[str], sentence2: list[str], similarPairs: list[list[str]]
    ) -> bool:
        """Union-Find to group similar words and check sentence equivalence.

        Intuition:
            Words connected by similarity pairs form equivalence classes. If two
            words in corresponding positions belong to the same class, the sentences
            are similar.

        Approach:
            1. Assign each unique word an integer index.
            2. Use Union-Find to merge indices of each similar pair.
            3. For every position, verify both words share the same root.

        Complexity:
            Time: O(P * α(P) + L) where P = len(similarPairs), L = sentence length
            Space: O(P)
        """
        if len(sentence1) != len(sentence2):
            return False
        num_pairs = len(similarPairs)
        parent = list(range(num_pairs << 1))

        def find(x: int) -> int:
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        word_index: dict[str, int] = {}
        idx = 0
        for word_a, word_b in similarPairs:
            if word_a not in word_index:
                word_index[word_a] = idx
                idx += 1
            if word_b not in word_index:
                word_index[word_b] = idx
                idx += 1
            parent[find(word_index[word_a])] = find(word_index[word_b])

        for i in range(len(sentence1)):
            if sentence1[i] == sentence2[i]:
                continue
            if (
                sentence1[i] not in word_index
                or sentence2[i] not in word_index
                or find(word_index[sentence1[i]]) != find(word_index[sentence2[i]])
            ):
                return False
        return True
