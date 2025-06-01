from collections import Counter
from typing import List


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        """Sliding window with Counter approach

        Intuition:
        Since all words are of the same length, we can use a sliding window approach.
        We need to find all starting indices where a permutation of all words appears.

        Approach:
        1. Create a counter of all words to track their frequencies
        2. For each possible starting position (0 to word_length-1), use a sliding window:
           - Add words to current counter and track valid words count
           - When a word appears more times than in the target counter, shrink window
           - When we have all required words, add the starting index to result
        3. Return all valid starting indices

        Complexity:
        Time: O(N * M), where N is the length of string s and M is the total length of all words
        Space: O(K), where K is the number of unique words in the words list
        """
        if not s or not words:
            return []

        word_count = Counter(words)
        string_length, word_count_total = len(s), len(words)
        word_length = len(words[0])
        result = []

        # Start from each possible position (0 to word_length-1)
        for start_pos in range(word_length):
            current_count = Counter()
            left = right = start_pos
            valid_word_count = 0

            while right + word_length <= string_length:
                # Get the next word in the window
                current_word = s[right:right + word_length]
                right += word_length

                # If current word is not in our target words, reset the window
                if current_word not in word_count:
                    left = right
                    current_count.clear()
                    valid_word_count = 0
                    continue

                # Add the current word to our counter
                current_count[current_word] += 1
                valid_word_count += 1

                # Shrink window if the current word appears more times than needed
                while current_count[current_word] > word_count[current_word]:
                    removed_word = s[left:left + word_length]
                    left += word_length
                    current_count[removed_word] -= 1
                    valid_word_count -= 1

                # If we have all required words, add the starting index
                if valid_word_count == word_count_total:
                    result.append(left)

        return result
