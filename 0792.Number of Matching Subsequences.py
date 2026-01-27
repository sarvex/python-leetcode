from collections import defaultdict, deque


class Solution:
    def numMatchingSubseq(self, s: str, words: list[str]) -> int:
        """Match words as subsequences using character-indexed queues.

        Intuition:
            Instead of checking each word independently against s, group words
            by their current needed character and process them as we iterate s.

        Approach:
            1. Group all words into queues indexed by their first character.
            2. Iterate through each character of s.
            3. For each matching word, pop it from the queue and either count it
               as complete or re-enqueue the remaining suffix under its next character.

        Complexity:
            Time: O(n + sum(len(word) for word in words)) where n = len(s)
            Space: O(m) where m = total characters across all words
        """
        char_queues: defaultdict[str, deque[str]] = defaultdict(deque)
        for word in words:
            char_queues[word[0]].append(word)
        result = 0
        for char in s:
            for _ in range(len(char_queues[char])):
                word = char_queues[char].popleft()
                if len(word) == 1:
                    result += 1
                else:
                    char_queues[word[1]].append(word[1:])
        return result
