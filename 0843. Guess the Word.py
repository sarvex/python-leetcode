class Solution:
    def findSecretWord(self, words: list[str], master: "Master") -> None:
        """Frequency-based word selection with elimination.

        Intuition:
            Choose the word with highest character-position frequency score
            to maximize information gain, then eliminate non-matching candidates.

        Approach:
            1. Compute character frequency at each position across all words.
            2. Score each word by summing its characters' frequencies.
            3. Guess the highest-scoring word, then filter candidates by match count.

        Complexity:
            Time: O(n^2) in the worst case for filtering
            Space: O(n)
        """
        position_frequencies: list[dict[str, int]] = []
        for pos in range(6):
            freq: dict[str, int] = {}
            for word in words:
                freq[word[pos]] = freq.get(word[pos], 0) + 1
            position_frequencies.append(freq)

        def compute_score(word: str) -> int:
            return sum(position_frequencies[i][word[i]] for i in range(len(word)))

        def count_common_chars(word1: str, word2: str) -> int:
            return sum(word1[i] == word2[i] for i in range(6))

        words.sort(key=compute_score)

        while len(words) > 0:
            candidate = words.pop()
            matches = master.guess(candidate)
            if matches == 6:
                break
            words = [w for w in words if matches == count_common_chars(w, candidate)]
